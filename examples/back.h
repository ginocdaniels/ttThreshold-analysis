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








  static std::pair<ROOT::VecOps::RVec<int>, ROOT::VecOps::RVec<float>> match_leptons_with_z0(
      const ROOT::VecOps::RVec<TLorentzVector>& mc_tlvs,
      const ROOT::VecOps::RVec<TLorentzVector>& reco_tlvs,
      const ROOT::VecOps::RVec<edm4hep::Vector3d>& mc_vertices,
      float deltaR_threshold) {
    ROOT::VecOps::RVec<int> reco_indices(mc_tlvs.size(), -1);
    ROOT::VecOps::RVec<float> z0_values;
    z0_values.reserve(mc_tlvs.size());
    std::vector<bool> used(reco_tlvs.size(), false);

    // Compute z0 for all MC leptons
    for (size_t i = 0; i < mc_tlvs.size() && i < mc_vertices.size(); ++i) {
      TVector3 x(mc_vertices[i].x, mc_vertices[i].y, mc_vertices[i].z);
      TVector3 p(mc_tlvs[i].Px(), mc_tlvs[i].Py(), mc_tlvs[i].Pz());
      float z0 = FCCAnalyses::myUtils::get_z0(x, p);
      z0_values.push_back(z0);
    }
    // // Fill with default 0.0 if vertices are fewer than tlvs
    // while (z0_values.size() < mc_tlvs.size()) {
    //   z0_values.push_back(-1);
    // }

    // Perform truth matching
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

    return std::make_pair(reco_indices, z0_values);
  }

static std::pair<ROOT::VecOps::RVec<int>, ROOT::VecOps::RVec<int>> getJetMotherPdgId(
    const ROOT::VecOps::RVec<fastjet::PseudoJet>& jets,
    const ROOT::VecOps::RVec<edm4hep::MCParticleData>& mcParticles,
    const ROOT::VecOps::RVec<int>& recIndices,
    const ROOT::VecOps::RVec<int>& mcIndices,
    const ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>& recoParticles,
    const ROOT::VecOps::RVec<int>& Particle0, // Parent indices (MCParticle#0.parents)
    const ROOT::VecOps::RVec<int>& Particle1, // Daughter indices (MCParticle#1.daughters)
    float max_angle = 0.3) {
  ROOT::VecOps::RVec<int> jetFlavors(jets.size(), 0);
  ROOT::VecOps::RVec<int> motherPdgIds(jets.size(), 0);

  // Get eta and phi for all MC particles
  auto partonEta = MCParticle::get_eta(mcParticles);
  auto partonPhi = MCParticle::get_phi(mcParticles);

  for (size_t j = 0; j < jets.size(); ++j) {
    const auto& jet = jets[j];
    float jetEta = jet.eta();
    float jetPhi = jet.phi_std();

    for (size_t i = 0; i < mcParticles.size(); ++i) {
      const auto& parton = mcParticles[i];
      // Select partons: quarks (|PDG| <= 5) or gluons (PDG == 21)
      // Status 70-80 (Pythia8 shower) or 2 (Pythia6 final state)
      if ((std::abs(parton.PDG) > 5 && parton.PDG != 21) ||
          ((parton.generatorStatus > 80 || parton.generatorStatus < 70) && parton.generatorStatus != 2)) {
        continue;
      }

      // Calculate angular distance
      float deta = jetEta - partonEta[i];
      float dphi = std::abs(jetPhi - partonPhi[i]);
      if (dphi > M_PI) dphi = 2 * M_PI - dphi;
      float angle = std::sqrt(deta * deta + dphi * dphi);

      if (angle <= max_angle) {
        int current_pdg = std::abs(parton.PDG);
        bool update_mother = false;

        // Flavor assignment: prefer heavier quarks over gluons
        if (jetFlavors[j] == 0 || jetFlavors[j] == 21) {
          jetFlavors[j] = current_pdg;
          update_mother = true;
        } else if (parton.PDG != 21) {
          int new_flavor = std::max(jetFlavors[j], current_pdg);
          if (new_flavor > jetFlavors[j]) {
            jetFlavors[j] = new_flavor;
            update_mother = true;
          }
        }

        if (update_mother && parton.parents_begin < parton.parents_end &&
            parton.parents_begin < Particle0.size()) {
          int selected_mother_pdg = 0;
          int selected_parent_idx = -1;
          // Check all immediate parents
          for (unsigned int p = parton.parents_begin; p < parton.parents_end && p < Particle0.size(); ++p) {
            int parent_idx = Particle0[p];
            if (parent_idx < 0 || parent_idx >= mcParticles.size()) continue;
            int parent_pdg = std::abs(mcParticles[parent_idx].PDG);

            // Exclude leptons as mothers for quark-flavored jets
            if (jetFlavors[j] >= 1 && jetFlavors[j] <= 5 &&
                parent_pdg >= 11 && parent_pdg <= 16) {
              continue;
            }

            // Validate mother by checking daughters
            bool flavor_match = false;
            const auto& parent = mcParticles[parent_idx];
            if (parent.daughters_begin < parent.daughters_end &&
                parent.daughters_begin < Particle1.size()) {
              for (unsigned int d = parent.daughters_begin; d < parent.daughters_end && d < Particle1.size(); ++d) {
                int daughter_idx = Particle1[d];
                if (daughter_idx >= 0 && daughter_idx < mcParticles.size()) {
                  int daughter_pdg = std::abs(mcParticles[daughter_idx].PDG);
                  if (daughter_pdg == jetFlavors[j]) {
                    flavor_match = true;
                    break;
                  }
                }
              }
            }

            if (flavor_match) {
              selected_mother_pdg = parent_pdg;
              selected_parent_idx = parent_idx;
              break; // Use the first valid mother
            }
          }

          // Only update if a valid mother was found
          if (selected_mother_pdg != 0) {
            motherPdgIds[j] = selected_mother_pdg;
          }

          // Debug output
          std::cout << "Jet " << j << " flavor " << jetFlavors[j]
                    << ", parton " << i << " PDG " << parton.PDG
                    << ", parents_begin " << parton.parents_begin
                    << ", parents_end " << parton.parents_end
                    << ", selected mother PDG " << selected_mother_pdg
                    << ", parent idx " << selected_parent_idx << std::endl;
          if (selected_parent_idx >= 0) {
            const auto& parent = mcParticles[selected_parent_idx];
            std::cout << "  Parent daughters: ";
            for (unsigned int d = parent.daughters_begin; d < parent.daughters_end && d < Particle1.size(); ++d) {
              int daughter_idx = Particle1[d];
              if (daughter_idx >= 0 && daughter_idx < mcParticles.size()) {
                std::cout << mcParticles[daughter_idx].PDG << " ";
              }
            }
            std::cout << std::endl;
          }
        }
      }
    }
  }

  return std::make_pair(jetFlavors, motherPdgIds);
}
  
};

} // namespace FCCAnalyses