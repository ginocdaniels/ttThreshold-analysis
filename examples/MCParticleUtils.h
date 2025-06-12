#ifndef MCPARTICLEUTILS_H
#define MCPARTICLEUTILS_H

#include "FCCAnalyses/myUtils.h"
#include "FCCAnalyses/MCParticle.h"
#include <iostream>

namespace FCCAnalyses {
namespace MCParticleUtils {

ROOT::VecOps::RVec<edm4hep::MCParticleData> get_leptonic_tau_daughters_from_W(
    const ROOT::VecOps::RVec<edm4hep::MCParticleData>& taus,
    const ROOT::VecOps::RVec<edm4hep::MCParticleData>& mc_particles,
    const ROOT::VecOps::RVec<int>& daughter_indices,
    const ROOT::VecOps::RVec<int>& parent_indices) {
  ROOT::VecOps::RVec<edm4hep::MCParticleData> result;
  const size_t max_daughters = 10; // Reasonable limit for tau decays
  std::cout << "Event: Processing " << taus.size() << " input taus" << std::endl;
  if (taus.empty()) {
    std::cout << "  No taus provided, returning empty result" << std::endl;
    return result;
  }
  if (daughter_indices.empty()) {
    std::cout << "  No daughter indices provided" << std::endl;
    return result;
  }
  if (parent_indices.empty()) {
    std::cout << "  No parent indices provided" << std::endl;
    return result;
  }
  for (size_t i = 0; i < taus.size(); ++i) {
    const auto& tau = taus[i];
    std::cout << "  Tau " << i << ": PDG = " << tau.PDG 
              << ", parents_begin = " << tau.parents_begin 
              << ", parents_end = " << tau.parents_end 
              << ", daughters_begin = " << tau.daughters_begin 
              << ", daughters_end = " << tau.daughters_end << std::endl;
    if (std::abs(tau.PDG) != 15) {
      std::cout << "    Not a tau, skipping" << std::endl;
      continue;
    }
    // Verify tau comes from W boson
    ROOT::VecOps::RVec<int> parent_idx = myUtils::getMC_parent(0, taus, parent_indices);
    int parent_id = parent_idx[i];
    std::cout << "    Parent index = " << parent_id << std::endl;
    if (parent_id == -999 || parent_id < 0 || parent_id >= mc_particles.size()) {
      std::cout << "    Invalid parent index, skipping" << std::endl;
      continue;
    }
    int parent_pdg = mc_particles[parent_id].PDG;
    std::cout << "    Parent PDG = " << parent_pdg << std::endl;
    if (std::abs(parent_pdg) != 24) {
      std::cout << "    Tau not from W boson, skipping" << std::endl;
      continue;
    }
    // Check daughters using DaughterIndices
    std::cout << "    Checking daughters" << std::endl;
    for (size_t d = 0; d < max_daughters; ++d) {
      ROOT::VecOps::RVec<int> daughter_idx = myUtils::getMC_daughter(d, taus, daughter_indices);
      int idx = daughter_idx[i];
      std::cout << "      Daughter " << d << ": index = " << idx << std::endl;
      if (idx == -999) {
        std::cout << "        No more daughters" << std::endl;
        break;
      }
      if (idx < 0 || idx >= mc_particles.size()) {
        std::cout << "        Invalid daughter index, skipping" << std::endl;
        continue;
      }
      const auto& daughter = mc_particles[idx];
      std::cout << "        Daughter PDG = " << daughter.PDG << std::endl;
      if (std::abs(daughter.PDG) == 11 || std::abs(daughter.PDG) == 13) {
        std::cout << "        Adding electron/muon daughter" << std::endl;
        result.push_back(daughter);
      } else {
        std::cout << "        Not an electron/muon, skipping" << std::endl;
      }
    }
  }
  std::cout << "Event: Returning " << result.size() << " daughters" << std::endl;
  return result;
}

} // namespace MCParticleUtils
} // namespace FCCAnalyses

#endif