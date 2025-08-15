#!/usr/bin/env python3
"""
Value Archaeology Study Implementation
Analyzes genetic selection platforms for embedded values and biases
"""

import json
from datetime import datetime
from typing import Dict, List, Any
import os

class ValueArchaeologyAnalyzer:
    def __init__(self):
        self.analysis_framework = {
            "trait_categorization": {
                "positive_traits": [],
                "negative_traits": [],
                "neutral_traits": [],
                "bias_indicators": []
            },
            "interface_language": {
                "enhancement_terms": [],
                "medical_terms": [],
                "optimization_language": [],
                "value_loaded_terms": []
            },
            "visual_representations": {
                "imagery_analysis": [],
                "color_associations": [],
                "layout_priorities": []
            },
            "default_settings": {
                "auto_recommendations": [],
                "preset_configurations": [],
                "implicit_assumptions": []
            }
        }
        self.platforms = []
        self.results = {}
    
    def analyze_platform(self, platform_name: str, platform_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze a single platform for embedded values"""
        analysis = {
            "platform": platform_name,
            "timestamp": datetime.now().isoformat(),
            "embedded_values": {},
            "bias_score": 0,
            "value_categories": []
        }
        
        # Trait Categorization Analysis
        trait_bias = self._analyze_trait_categorization(platform_data.get("traits", {}))
        analysis["embedded_values"]["trait_bias"] = trait_bias
        analysis["bias_score"] += trait_bias["bias_score"]
        
        # Interface Language Analysis
        language_bias = self._analyze_interface_language(platform_data.get("interface", {}))
        analysis["embedded_values"]["language_bias"] = language_bias
        analysis["bias_score"] += language_bias["bias_score"]
        
        # Default Settings Analysis
        defaults_bias = self._analyze_default_settings(platform_data.get("defaults", {}))
        analysis["embedded_values"]["defaults_bias"] = defaults_bias
        analysis["bias_score"] += defaults_bias["bias_score"]
        
        # Categorize overall value system
        analysis["value_categories"] = self._categorize_values(analysis["embedded_values"])
        
        return analysis
    
    def _analyze_trait_categorization(self, traits_data: Dict) -> Dict[str, Any]:
        """Analyze how traits are categorized and prioritized"""
        bias_indicators = []
        bias_score = 0
        
        # Check for enhancement vs. medical framing
        if "enhancements" in traits_data:
            bias_indicators.append("Enhancement framing present")
            bias_score += 2
            
        # Check for implicit value hierarchies
        if "priority_traits" in traits_data:
            priority_traits = traits_data["priority_traits"]
            if any(trait in ["intelligence", "athleticism", "beauty"] for trait in priority_traits):
                bias_indicators.append("Traditional enhancement values prioritized")
                bias_score += 3
                
        # Check for disability framing
        if "medical_conditions" in traits_data:
            conditions = traits_data["medical_conditions"]
            if len(conditions) > len(traits_data.get("enhancements", [])):
                bias_indicators.append("Medical model bias detected")
                bias_score += 2
        
        return {
            "bias_indicators": bias_indicators,
            "bias_score": bias_score,
            "analysis": "Trait categorization reveals embedded assumptions about human value"
        }
    
    def _analyze_interface_language(self, interface_data: Dict) -> Dict[str, Any]:
        """Analyze language choices in interface design"""
        value_loaded_terms = []
        bias_score = 0
        
        text_content = interface_data.get("text", "").lower()
        
        # Enhancement language
        enhancement_terms = ["optimize", "improve", "enhance", "upgrade", "perfect"]
        found_enhancement = [term for term in enhancement_terms if term in text_content]
        if found_enhancement:
            value_loaded_terms.extend(found_enhancement)
            bias_score += len(found_enhancement)
            
        # Deficit language
        deficit_terms = ["correct", "fix", "eliminate", "prevent", "reduce"]
        found_deficit = [term for term in deficit_terms if term in text_content]
        if found_deficit:
            value_loaded_terms.extend(found_deficit)
            bias_score += len(found_deficit) * 1.5  # Higher weight for deficit framing
        
        return {
            "value_loaded_terms": value_loaded_terms,
            "bias_score": bias_score,
            "analysis": "Language choices reveal embedded value assumptions"
        }
    
    def _analyze_default_settings(self, defaults_data: Dict) -> Dict[str, Any]:
        """Analyze default configurations for implicit assumptions"""
        implicit_assumptions = []
        bias_score = 0
        
        # Check pre-selected traits
        if "preselected_traits" in defaults_data:
            preselected = defaults_data["preselected_traits"]
            if preselected:
                implicit_assumptions.append(f"Pre-selects {len(preselected)} traits by default")
                bias_score += len(preselected)
        
        # Check recommendation algorithms
        if "auto_recommend" in defaults_data and defaults_data["auto_recommend"]:
            implicit_assumptions.append("Automatic recommendations enabled by default")
            bias_score += 3
        
        # Check opt-out vs opt-in patterns
        if "opt_out_enhancements" in defaults_data:
            implicit_assumptions.append("Enhancement opt-out pattern suggests normalization")
            bias_score += 2
        
        return {
            "implicit_assumptions": implicit_assumptions,
            "bias_score": bias_score,
            "analysis": "Default settings embed value judgments about desirable modifications"
        }
    
    def _categorize_values(self, embedded_values: Dict) -> List[str]:
        """Categorize the overall value system of the platform"""
        categories = []
        
        total_bias = sum([v.get("bias_score", 0) for v in embedded_values.values()])
        
        if total_bias > 8:
            categories.append("High value embedding")
        elif total_bias > 4:
            categories.append("Moderate value embedding")
        else:
            categories.append("Low value embedding")
            
        # Specific value categories
        trait_bias = embedded_values.get("trait_bias", {})
        if "Traditional enhancement values prioritized" in trait_bias.get("bias_indicators", []):
            categories.append("Enhancement-oriented")
            
        if "Medical model bias detected" in trait_bias.get("bias_indicators", []):
            categories.append("Medical-model-oriented")
            
        language_bias = embedded_values.get("language_bias", {})
        if language_bias.get("bias_score", 0) > 3:
            categories.append("Value-loaded language")
        
        return categories
    
    def run_analysis(self, platforms_data: Dict[str, Dict]) -> Dict[str, Any]:
        """Run the complete value archaeology analysis"""
        print("Starting Value Archaeology Analysis...")
        
        results = {
            "study_metadata": {
                "experiment_id": "EXP003",
                "analysis_date": datetime.now().isoformat(),
                "platforms_analyzed": len(platforms_data),
                "framework_version": "1.0"
            },
            "platform_analyses": {},
            "summary_statistics": {},
            "hypothesis_validation": {}
        }
        
        # Analyze each platform
        for platform_name, platform_data in platforms_data.items():
            print(f"Analyzing platform: {platform_name}")
            analysis = self.analyze_platform(platform_name, platform_data)
            results["platform_analyses"][platform_name] = analysis
        
        # Generate summary statistics
        results["summary_statistics"] = self._generate_summary_stats(results["platform_analyses"])
        
        # Test hypothesis
        results["hypothesis_validation"] = self._validate_hypothesis(results["platform_analyses"])
        
        return results
    
    def _generate_summary_stats(self, analyses: Dict) -> Dict[str, Any]:
        """Generate summary statistics across all platforms"""
        total_platforms = len(analyses)
        high_bias_platforms = sum(1 for a in analyses.values() if a["bias_score"] > 8)
        
        all_categories = []
        for analysis in analyses.values():
            all_categories.extend(analysis["value_categories"])
        
        category_counts = {}
        for category in set(all_categories):
            category_counts[category] = all_categories.count(category)
        
        return {
            "total_platforms": total_platforms,
            "high_bias_platforms": high_bias_platforms,
            "high_bias_percentage": (high_bias_platforms / total_platforms) * 100,
            "category_distribution": category_counts,
            "average_bias_score": sum(a["bias_score"] for a in analyses.values()) / total_platforms
        }
    
    def _validate_hypothesis(self, analyses: Dict) -> Dict[str, Any]:
        """Test the research hypothesis against collected data"""
        summary = self._generate_summary_stats(analyses)
        
        # Success criteria from experiment plan:
        # >80% of platforms show embedded values
        platforms_with_values = sum(1 for a in analyses.values() if a["bias_score"] > 0)
        value_embedding_rate = (platforms_with_values / len(analyses)) * 100
        
        # Systematic bias patterns across platforms
        common_patterns = []
        if summary["category_distribution"].get("Enhancement-oriented", 0) > len(analyses) * 0.5:
            common_patterns.append("Enhancement bias pattern")
        if summary["category_distribution"].get("Medical-model-oriented", 0) > len(analyses) * 0.5:
            common_patterns.append("Medical model bias pattern")
        if summary["category_distribution"].get("Value-loaded language", 0) > len(analyses) * 0.6:
            common_patterns.append("Value-loaded language pattern")
        
        hypothesis_supported = value_embedding_rate >= 80 and len(common_patterns) >= 2
        
        return {
            "hypothesis": "Genetic selection technologies embed value systems that privilege certain forms of human existence",
            "value_embedding_rate": value_embedding_rate,
            "systematic_patterns": common_patterns,
            "hypothesis_supported": hypothesis_supported,
            "evidence": {
                "meets_80_percent_threshold": value_embedding_rate >= 80,
                "systematic_patterns_found": len(common_patterns) >= 2,
                "average_bias_score": summary["average_bias_score"]
            }
        }

def create_mock_platform_data():
    """Create mock data for genetic selection platforms for analysis"""
    return {
        "GenePerfect": {
            "traits": {
                "enhancements": ["intelligence", "athleticism", "beauty", "longevity"],
                "medical_conditions": ["huntington", "cystic_fibrosis"],
                "priority_traits": ["intelligence", "beauty"]
            },
            "interface": {
                "text": "Optimize your child's genetic potential. Enhance intelligence and eliminate genetic defects. Perfect your family's future."
            },
            "defaults": {
                "preselected_traits": ["intelligence", "disease_resistance"],
                "auto_recommend": True,
                "opt_out_enhancements": True
            }
        },
        "GeneticChoice": {
            "traits": {
                "enhancements": ["cognitive_ability", "physical_fitness"],
                "medical_conditions": ["sickle_cell", "tay_sachs", "hemophilia", "muscular_dystrophy"],
                "priority_traits": ["cognitive_ability"]
            },
            "interface": {
                "text": "Make informed genetic choices. Improve health outcomes and reduce genetic risks for your family."
            },
            "defaults": {
                "preselected_traits": ["disease_resistance"],
                "auto_recommend": False,
                "opt_out_enhancements": False
            }
        },
        "HealthyGenes": {
            "traits": {
                "medical_conditions": ["diabetes_risk", "heart_disease", "cancer_predisposition", "alzheimer_risk"],
                "enhancements": ["immune_system"],
                "priority_traits": ["disease_prevention"]
            },
            "interface": {
                "text": "Prevent genetic diseases and secure your child's health future. Medical-grade genetic screening and correction."
            },
            "defaults": {
                "preselected_traits": ["diabetes_prevention", "cancer_prevention"],
                "auto_recommend": True,
                "opt_out_enhancements": False
            }
        },
        "FutureGen": {
            "traits": {
                "enhancements": ["intelligence", "creativity", "social_skills", "athleticism", "longevity"],
                "medical_conditions": ["genetic_disorders"],
                "priority_traits": ["intelligence", "creativity", "athleticism"]
            },
            "interface": {
                "text": "Upgrade your child's genetic code. Enhance capabilities and eliminate limitations. Build the next generation."
            },
            "defaults": {
                "preselected_traits": ["intelligence", "athleticism", "creativity"],
                "auto_recommend": True,
                "opt_out_enhancements": True
            }
        },
        "GeneGuardian": {
            "traits": {
                "medical_conditions": ["rare_diseases", "common_conditions", "behavioral_disorders"],
                "enhancements": ["disease_resistance"],
                "priority_traits": ["health_protection"]
            },
            "interface": {
                "text": "Protect your child from genetic diseases. Medical genetic screening with protective modifications available."
            },
            "defaults": {
                "preselected_traits": [],
                "auto_recommend": False,
                "opt_out_enhancements": False
            }
        }
    }

if __name__ == "__main__":
    print("Value Archaeology Study - EXP003")
    print("="*50)
    
    # Initialize analyzer
    analyzer = ValueArchaeologyAnalyzer()
    
    # Create mock platform data (in real study, this would be actual platform data)
    platforms_data = create_mock_platform_data()
    
    # Run analysis
    results = analyzer.run_analysis(platforms_data)
    
    # Save results
    os.makedirs("../data", exist_ok=True)
    
    with open("../data/value_archaeology_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    # Display key findings
    print("\nKEY FINDINGS:")
    print(f"Platforms analyzed: {results['summary_statistics']['total_platforms']}")
    print(f"Platforms with embedded values: {results['hypothesis_validation']['value_embedding_rate']:.1f}%")
    print(f"Average bias score: {results['summary_statistics']['average_bias_score']:.2f}")
    print(f"Hypothesis supported: {results['hypothesis_validation']['hypothesis_supported']}")
    
    print("\nSystematic patterns found:")
    for pattern in results['hypothesis_validation']['systematic_patterns']:
        print(f"- {pattern}")
    
    print(f"\nDetailed results saved to: data/value_archaeology_results.json")