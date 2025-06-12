


#pragma once
#include <cmath>
#include <vector>
#include <math.h>

#include "TLorentzVector.h"
#include "ROOT/RVec.hxx"
#include "edm4hep/ReconstructedParticleData.h"
#include "edm4hep/MCParticleData.h"
#include "edm4hep/ParticleIDData.h"
#include "ReconstructedParticle2MC.h"



namespace FCCAnalyses {
// Takes in collection of mc tlv and reco tlv and a delta R threshold and returns a vector of indices of the reco tlv that are matched to the mc tlv
// If no match is found, the index is -1
struct TruthMatching {
  static ROOT::VecOps::RVec<int> match_leptons(
      const ROOT::VecOps::RVec<TLorentzVector>& mc_tlvs,
      const ROOT::VecOps::RVec<TLorentzVector>& reco_tlvs,
      float deltaR_threshold) {
    ROOT::VecOps::RVec<int> reco_indices(mc_tlvs.size(), -1);
    std::vector<bool> used(reco_tlvs.size(), false);
    for (size_t i = 0; i < mc_tlvs.size(); ++i) {
      float min_dR = deltaR_threshold;
      int best_reco_idx = -1;
      for (size_t j = 0; j < reco_tlvs.size(); ++j) {
        if (used[j]) continue;
        float dR = mc_tlvs[i].DeltaR(reco_tlvs[j]);
        if (dR < min_dR) {
          min_dR = dR;
          best_reco_idx = j;
        }
      }
      if (best_reco_idx >= 0) {
        reco_indices[i] = best_reco_idx;
        used[best_reco_idx] = true;
      }
    }
    return reco_indices;
  }
 // Delta R calc between two tlv collections
  static ROOT::VecOps::RVec<float> Delta_R_calc(
      const ROOT::VecOps::RVec<TLorentzVector>& mc_tlvs,
      const ROOT::VecOps::RVec<TLorentzVector>& reco_tlvs) {
    ROOT::VecOps::RVec<float> delta_r_values;
    delta_r_values.reserve(mc_tlvs.size() * reco_tlvs.size());
    for (size_t i = 0; i < mc_tlvs.size(); ++i) {
      for (size_t j = 0; j < reco_tlvs.size(); ++j) {
        float dR = mc_tlvs[i].DeltaR(reco_tlvs[j]);
        delta_r_values.push_back(dR);
      }
    }
    
    return delta_r_values;
  }
  // Delta R calc between two tlv collections, returns the minimum delta R value for each lepton
   static ROOT::VecOps::RVec<float> Delta_R_min_calc(
      const ROOT::VecOps::RVec<TLorentzVector>& tlvs_1_jets,
      const ROOT::VecOps::RVec<TLorentzVector>& tlvs_2_leptons){
        ROOT::VecOps::RVec<float> delta_r_values;
        delta_r_values.reserve(tlvs_2_leptons.size());
        for (size_t i = 0; i < tlvs_2_leptons.size(); ++i) {
            float min_dR = std::numeric_limits<float>::max();
            for (size_t j = 0; j < tlvs_1_jets.size(); ++j) {
                float dR = tlvs_2_leptons[i].DeltaR(tlvs_1_jets[j]);
                if (dR < min_dR) {
                    min_dR = dR;
                }
            }
            delta_r_values.push_back(min_dR);
        }
        return delta_r_values;
      }













  // Compute z0 for all particles from a collection of vertices and tlvs, was used to keep track of z0 vals for truth matched leptons then look at correlation between z0 and D Iso
  static ROOT::VecOps::RVec<float> compute_z0(
      const ROOT::VecOps::RVec<edm4hep::Vector3d>& vertices,
      const ROOT::VecOps::RVec<TLorentzVector>& tlvs) {
    ROOT::VecOps::RVec<float> z0_values;
    z0_values.reserve(vertices.size());
    for (size_t i = 0; i < vertices.size(); ++i) {
      TVector3 x(vertices[i].x, vertices[i].y, vertices[i].z);
      TVector3 p(tlvs[i].Px(), tlvs[i].Py(), tlvs[i].Pz());
      float z0 = FCCAnalyses::myUtils::get_z0(x, p);
      z0_values.push_back(z0);
    }
    return z0_values;
  }








  static Vec_i jetTruthFinder(std::vector<std::vector<int>> constituents, Vec_rp reco, Vec_mc mc, Vec_i mcind, bool findGluons = false) {
    // jet truth=finder: match the gen-level partons (eventually with gluons) with the jet constituents
    // matching by mimimizing the sum of dr of the parton and all the jet constituents 

    Vec_tlv genQuarks; // Lorentz-vector of potential partons (gen-level)
    Vec_i genQuarks_pdgId; // corresponding PDG ID
    for(size_t i = 0; i < mc.size(); ++i) {
        int pdgid = abs(mc.at(i).PDG);
        if(pdgid > 6 and not findGluons) continue; // only quarks 
        if(pdgid > 6 and pdgid != 21 and findGluons) continue; // only quarks and gluons
        TLorentzVector tlv;
        tlv.SetXYZM(mc.at(i).momentum.x,mc.at(i).momentum.y,mc.at(i).momentum.z,mc.at(i).mass);
        genQuarks.push_back(tlv);
        genQuarks_pdgId.push_back(mc.at(i).PDG);
    }

    Vec_tlv recoParticles; // Lorentz-vector of all reconstructed particles
    for(size_t i = 0; i < reco.size(); ++i) {
        auto & p = reco[i];
        TLorentzVector tlv;
        tlv.SetXYZM(p.momentum.x, p.momentum.y, p.momentum.z, p.mass);
        recoParticles.push_back(tlv);
    }

    Vec_i usedIdx;
    Vec_i result;
    for(size_t iJet = 0; iJet < constituents.size(); ++iJet) {
        Vec_d dr;
        for(size_t iGen = 0; iGen < genQuarks.size(); ++iGen) {
            if(std::find(usedIdx.begin(), usedIdx.end(), iGen) != usedIdx.end()) {
                dr.push_back(1e99); // set infinite dr, skip
                continue;
            }
            dr.push_back(0);
            for(size_t i = 0; i < constituents[iJet].size(); ++i) {
                dr[iGen] += recoParticles[constituents[iJet][i]].DeltaR(genQuarks[iGen]);
            }
        }
        int maxDrIdx = std::min_element(dr.begin(),dr.end()) - dr.begin();
        usedIdx.push_back(maxDrIdx);
        result.push_back(genQuarks_pdgId[maxDrIdx]);

    }
    return result;
 }
};

} // namespace FCCAnalyses
