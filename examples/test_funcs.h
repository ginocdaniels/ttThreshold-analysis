#pragma once
#include <cmath>
#include <vector>
#include <math.h>

#include "TLorentzVector.h"
#include "ROOT/RVec.hxx"
#include "edm4hep/ReconstructedParticleData.h"
#include "edm4hep/MCParticleData.h"
#include "edm4hep/ParticleIDData.h"


namespace FCCAnalyses {
namespace TestFuncs {
ROOT::VecOps::RVec<int> get_MCElectronMuonDaughters(
    const ROOT::VecOps::RVec<edm4hep::MCParticleData>& taus,
    const ROOT::VecOps::RVec<edm4hep::MCParticleData>& particles,
    const ROOT::VecOps::RVec<int>& daughter_indices) {
  ROOT::VecOps::RVec<int> result;
  for (const auto& tau : taus) {
   
    if (std::abs(tau.PDG) != 15) continue;
   
    for (unsigned j = tau.daughters_begin; j != tau.daughters_end; ++j) {
      int dau_idx = daughter_indices[j];
      if (dau_idx < 0 || dau_idx >= particles.size()) continue;
      int pdg = std::abs(particles[dau_idx].PDG);
      if (pdg == 11 || pdg == 13) { // Electron or muon
        result.push_back(dau_idx);
      }
    }
  }
  return result;
}
} // namespace TestFuncs
} // namespace FCCAnalyses