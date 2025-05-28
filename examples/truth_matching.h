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
};

} // namespace FCCAnalyses