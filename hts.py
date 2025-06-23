"""
Strategic HTS Codes for Trade Imbalance Analysis

This script identifies and categorizes the most important HTS codes for understanding
US trade dependencies and strategic import patterns that drive trade imbalances.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def define_strategic_hts_codes():
    """Define HTS codes by strategic importance categories."""
    
    strategic_codes = {
        "SEMICONDUCTORS & ELECTRONICS": {
            "description": "Critical for technology sector, concentrated in Asia",
            "trade_impact": "High - Major driver of China deficit",
            "dependency_level": "Critical",
            "codes": {
                "8541": "Semiconductors, diodes, transistors, photovoltaic cells",
                "8542": "Electronic integrated circuits (microprocessors, memory chips)", 
                "8471": "Computers and computer equipment",
                "8473": "Computer parts and accessories",
                "8517": "Telecommunications equipment (phones, networking)",
                "8528": "Reception/transmission apparatus for TV, radio",
                "9013": "Lasers, optical instruments",
                "8534": "Printed circuit boards"
            }
        },
        
        "CRITICAL MINERALS & MATERIALS": {
            "description": "Essential for clean energy, defense, technology",
            "trade_impact": "Medium-High - Strategic vulnerability", 
            "dependency_level": "Critical",
            "codes": {
                "2805": "Rare earth metals (lithium, cobalt, etc.)",
                "2844": "Radioactive elements (uranium, thorium)",
                "7108": "Gold and other precious metals",
                "2603": "Copper ores and concentrates",
                "2607": "Lead ores and concentrates", 
                "2608": "Zinc ores and concentrates",
                "8107": "Cadmium and articles thereof",
                "8109": "Zirconium and articles thereof",
                "2825": "Hydrazine, hydroxides (battery materials)"
            }
        },
        
        "PHARMACEUTICALS & MEDICAL": {
            "description": "Health security and pharmaceutical dependencies", 
            "trade_impact": "Medium-High - Exposed during COVID-19",
            "dependency_level": "High", 
            "codes": {
                "3004": "Pharmaceutical products (medicines)",
                "3002": "Human/animal blood, vaccines, toxins",
                "3006": "Pharmaceutical goods (first aid, contraceptives)",
                "3001": "Glands, organs for therapeutic use",
                "9021": "Medical/surgical appliances (pacemakers, hearing aids)",
                "9018": "Medical/surgical instruments", 
                "3822": "Diagnostic reagents",
                "2941": "Antibiotics"
            }
        },
        
        "ADVANCED MACHINERY & EQUIPMENT": {
            "description": "Industrial competitiveness and manufacturing capability",
            "trade_impact": "Medium - Manufacturing dependency",
            "dependency_level": "Medium-High",
            "codes": {
                "8456": "Machine tools (laser cutting, 3D printing)",
                "8477": "Injection molding machinery",
                "8479": "Industrial machinery and robots",
                "8486": "Semiconductor manufacturing equipment", 
                "8543": "Electrical machines and apparatus",
                "9031": "Measuring/testing instruments",
                "8428": "Lifting/loading machinery",
                "8441": "Paper/textile manufacturing machinery"
            }
        },
        
        "ENERGY & BATTERIES": {
            "description": "Energy transition and storage dependencies",
            "trade_impact": "High - Clean energy transition", 
            "dependency_level": "High",
            "codes": {
                "8507": "Electric batteries and storage",
                "8541": "Photovoltaic cells and solar panels", 
                "8502": "Electric generators and generating sets",
                "8503": "Parts for electric generators",
                "2710": "Petroleum oils and fuels",
                "8504": "Electrical transformers and converters"
            }
        },
        
        "TEXTILES & APPAREL": {
            "description": "Consumer goods, labor-intensive manufacturing",
            "trade_impact": "High - Large volume, price-sensitive",
            "dependency_level": "Medium",
            "codes": {
                "6109": "T-shirts, singlets, tank tops", 
                "6203": "Men's suits, jackets, trousers",
                "6204": "Women's suits, jackets, dresses",
                "6403": "Footwear with rubber/plastic soles",
                "6402": "Other footwear",
                "6307": "Made-up textile articles",
                "5208": "Cotton fabrics",
                "6302": "Bed linen, table linen"
            }
        },
        
        "FOOD & AGRICULTURE": {
            "description": "Food security and seasonal import dependencies", 
            "trade_impact": "Medium - Seasonal and specialty items",
            "dependency_level": "Medium",
            "codes": {
                "0306": "Shellfish (shrimp, lobster, crab)",
                "0303": "Frozen fish",
                "0804": "Dates, figs, pineapples, avocados", 
                "0901": "Coffee and coffee substitutes",
                "1701": "Cane/beet sugar",
                "2401": "Tobacco and tobacco products",
                "0713": "Dried legumes",
                "1806": "Chocolate and cocoa preparations"
            }
        },
        
        "TOYS & CONSUMER GOODS": {
            "description": "Discretionary consumer spending, manufacturing offshoring",
            "trade_impact": "Medium - Large volume consumer items", 
            "dependency_level": "Low-Medium",
            "codes": {
                "9503": "Toys and sporting goods",
                "9401": "Furniture and seating",
                "6913": "Statuettes, ornamental ceramics", 
                "4202": "Luggage, handbags, wallets",
                "9504": "Video games and playing cards",
                "6601": "Umbrellas and walking sticks",
                "9505": "Party supplies and decorations"
            }
        }
    }
    
    return strategic_codes

def create_hts_priority_matrix():
    """Create visualization showing HTS code priorities."""
    
    strategic_codes = define_strategic_hts_codes()
    
    # Create dataframe for analysis
    categories = []
    trade_impacts = []
    dependency_levels = []
    code_counts = []
    
    impact_mapping = {"High": 3, "Medium-High": 2.5, "Medium": 2, "Low-Medium": 1.5, "Low": 1}
    dependency_mapping = {"Critical": 3, "High": 2.5, "Medium-High": 2, "Medium": 1.5, "Low": 1}
    
    for category, info in strategic_codes.items():
        categories.append(category)
        trade_impacts.append(impact_mapping[info["trade_impact"].split(" - ")[0]])
        dependency_levels.append(dependency_mapping[info["dependency_level"]])
        code_counts.append(len(info["codes"]))
    
    # Create visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))
    fig.suptitle('Strategic HTS Codes: Priority Analysis for Trade Imbalance Understanding', 
                 fontsize=16, fontweight='bold')
    
    # Priority scatter plot
    scatter = ax1.scatter(trade_impacts, dependency_levels, 
                         s=[x*50 for x in code_counts], 
                         c=trade_impacts, cmap='RdYlBu_r', alpha=0.7)
    
    # Add category labels
    for i, cat in enumerate(categories):
        ax1.annotate(cat.replace(" & ", " &\n"), 
                    (trade_impacts[i], dependency_levels[i]), 
                    xytext=(5, 5), textcoords='offset points', 
                    fontsize=9, fontweight='bold')
    
    ax1.set_xlabel('Trade Impact Score', fontweight='bold')
    ax1.set_ylabel('US Dependency Level', fontweight='bold')
    ax1.set_title('HTS Category Priority Matrix', fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0.5, 3.5)
    ax1.set_ylim(0.5, 3.5)
    
    # Add quadrant labels
    ax1.text(1, 3, 'LOW IMPACT\nHIGH DEPENDENCY', ha='center', va='center',
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    ax1.text(3, 3, 'HIGH IMPACT\nHIGH DEPENDENCY\n(STRATEGIC PRIORITY)', ha='center', va='center',
             bbox=dict(boxstyle='round', facecolor='salmon', alpha=0.7))
    ax1.text(1, 1, 'LOW IMPACT\nLOW DEPENDENCY', ha='center', va='center',
             bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.7))
    ax1.text(3, 1, 'HIGH IMPACT\nLOW DEPENDENCY', ha='center', va='center',
             bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    # Code count by category
    ax2.barh(categories, code_counts, color=plt.cm.RdYlBu_r([x/3 for x in trade_impacts]))
    ax2.set_xlabel('Number of Key HTS Codes', fontweight='bold')
    ax2.set_title('HTS Code Coverage by Strategic Category', fontweight='bold')
    
    # Add value labels
    for i, count in enumerate(code_counts):
        ax2.text(count + 0.1, i, str(count), va='center', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/tmp/outputs/strategic_hts_priority_matrix.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_implementation_guide():
    """Create detailed implementation guide for HTS code analysis."""
    
    strategic_codes = define_strategic_hts_codes()
    
    guide = """# Strategic HTS Codes Implementation Guide

## 🎯 **Recommended Implementation Priority**

### **PHASE 1: CRITICAL DEPENDENCIES (Week 1-2)**
Focus on these codes first - they explain the largest trade imbalances and strategic vulnerabilities:

#### 🔴 **SEMICONDUCTORS** (Start here!)
```python
semiconductor_codes = [
    "8541", # Semiconductors, diodes, transistors  
    "8542", # Electronic integrated circuits (THE BIG ONE)
    "8471", # Computers and computer equipment
    "8517"  # Telecommunications equipment
]
```
**Why Priority**: 
- Explains majority of China trade deficit
- No domestic alternatives (US doesn't manufacture advanced chips)
- National security implications
- $200B+ annual imports

#### 🟠 **CRITICAL MINERALS**
```python
critical_mineral_codes = [
    "2805", # Rare earth metals (lithium, cobalt)
    "2844", # Radioactive elements  
    "8107", # Cadmium (batteries)
    "2825"  # Battery materials
]
```
**Why Priority**:
- Essential for electric vehicles, renewable energy
- China dominates global supply (60-80% market share)
- No easy substitutes
- National security and climate policy dependencies

### **PHASE 2: HIGH VOLUME IMPORTS (Week 3-4)**

#### 🟡 **TEXTILES & CONSUMER GOODS**
```python
consumer_codes = [
    "6109", # T-shirts, basic apparel
    "6403", # Footwear  
    "9503", # Toys
    "9401"  # Furniture
]
```
**Why Important**:
- High dollar volume
- Labor cost arbitrage explains trade patterns
- Tariff-sensitive categories
- Easy to understand for policy analysis

#### 🟢 **PHARMACEUTICALS**
```python
pharma_codes = [
    "3004", # Pharmaceutical products
    "3002", # Vaccines, medical biologics
    "9021", # Medical devices
    "3822"  # Diagnostic reagents
]
```
**Why Strategic**:
- COVID-19 exposed vulnerabilities
- Health security implications
- High-value, specialized products

### **PHASE 3: DETAILED ANALYSIS (Month 2)**

Add remaining categories for comprehensive understanding:
- Advanced machinery
- Energy equipment  
- Food/agriculture
- Other strategic materials

## 📊 **Data Collection Strategy**

### **HTS Code Data Sources**
1. **US Census Bureau Foreign Trade Division**
   - URL: https://www.census.gov/foreign-trade/statistics/
   - Format: Monthly imports by HTS code and country
   - Detail Level: 6-digit and 10-digit codes available

2. **USITC DataWeb** (Most Comprehensive)
   - URL: https://dataweb.usitc.gov/
   - Advantage: Interactive queries, multiple time periods
   - Free registration required

3. **Federal Reserve Economic Data (FRED)**
   - URL: https://fred.stlouisfed.org/
   - Good for: Aggregate trade indices and economic context

### **Recommended Query Structure**
```python
# Example query parameters
query_params = {
    'hts_codes': ['8541', '8542', '8471', '8517'],  # Semiconductors
    'countries': ['China', 'Taiwan', 'South Korea', 'Japan'],  # Key suppliers
    'time_period': '2020-2025',
    'data_type': 'imports',  # Focus on imports for dependency analysis
    'value_type': 'customs_value'  # Consistent valuation method
}
```

## 🔍 **Analysis Framework**

### **Key Metrics to Calculate**
1. **Import Dependency Ratio**: 
   ```python
   dependency_ratio = imports_by_country / total_imports_category
   ```

2. **Supply Concentration Index**:
   ```python  
   hhi_index = sum([market_share_i**2 for market_share_i in country_shares])
   ```

3. **Strategic Vulnerability Score**:
   ```python
   vulnerability = (import_dependency * supply_concentration * substitutability_factor)
   ```

### **Questions Your Analysis Can Answer**
- ✅ **Which countries control critical supply chains?**
- ✅ **How concentrated are strategic imports?** 
- ✅ **What imports have no domestic alternatives?**
- ✅ **Which trade deficits are strategic vs. economic choice?**
- ✅ **How do tariffs affect different types of imports?**

## 💡 **Strategic Insights You'll Uncover**

### **Semiconductors Example**:
```
Expected Finding: 
- 70%+ of semiconductor imports from China/Taiwan/South Korea
- US domestic production <10% of consumption  
- Trade deficit driven by necessity, not preference
- Tariffs create costs but don't reduce dependency
```

### **Textiles Example**:
```
Expected Finding:
- 40%+ from China, Vietnam, Bangladesh
- Labor cost differential explains trade pattern
- US production economically unviable at scale
- Tariffs shift suppliers but maintain deficit
```

### **Critical Minerals Example**:
```
Expected Finding:
- China controls 60-80% of rare earth processing
- Limited alternative suppliers
- Essential for green energy transition
- Strategic vulnerability vs. economic efficiency
```

## 🎯 **Implementation Timeline**

### **Week 1**: 
- Focus on HTS 8541, 8542 (semiconductors)
- Query China, Taiwan, South Korea data
- Calculate basic dependency ratios

### **Week 2**:
- Add critical minerals (HTS 2805, 2844)
- Expand to Japan, Singapore suppliers  
- Create supply concentration analysis

### **Week 3-4**:
- Add high-volume consumer goods
- Include NAFTA partners for comparison
- Develop strategic vs. economic trade classification

### **Month 2**:
- Complete strategic categories
- Create policy-relevant summaries
- Prepare trade dependency dashboard

## ⚡ **Quick Start Code Template**

```python
import pandas as pd

# Download semiconductor imports by country
semiconductor_imports = get_hts_data(
    codes=['8541', '8542'],
    countries=['China', 'Taiwan', 'South Korea', 'Japan'],
    years=range(2020, 2026)
)

# Calculate dependency metrics
total_semi_imports = semiconductor_imports.groupby('Year')['Value'].sum()
china_share = semiconductor_imports[
    semiconductor_imports['Country'] == 'China'
].groupby('Year')['Value'].sum() / total_semi_imports

# Create strategic analysis
strategic_dependency = {
    'category': 'Semiconductors',
    'china_market_share': china_share.mean(),
    'total_value': total_semi_imports.sum(),
    'vulnerability_level': 'Critical'
}
```

## 🚨 **Key Success Factors**

1. **Start Small**: Begin with 4-6 key HTS codes
2. **Focus on Story**: Each code should explain a trade pattern
3. **Country Context**: Same HTS code tells different stories by supplier
4. **Time Trends**: Track how dependencies evolved over time
5. **Policy Relevance**: Connect to current trade policy debates

---
*Strategy: Explain trade imbalances through strategic dependencies*  
*Goal: Show which deficits are choices vs. necessities*
"""
    
    with open('/tmp/outputs/hts_implementation_guide.md', 'w') as f:
        f.write(guide)
    
    print("📋 Implementation Guide Generated")
    print("💾 Saved to: /tmp/outputs/hts_implementation_guide.md")

def create_hts_code_reference():
    """Create a comprehensive HTS code reference sheet."""
    
    strategic_codes = define_strategic_hts_codes()
    
    # Create reference dataframe
    reference_data = []
    for category, info in strategic_codes.items():
        for code, description in info["codes"].items():
            reference_data.append({
                'HTS_Code': code,
                'Description': description,
                'Category': category,
                'Trade_Impact': info["trade_impact"],
                'Dependency_Level': info["dependency_level"],
                'Strategic_Note': info["description"]
            })
    
    reference_df = pd.DataFrame(reference_data)
    
    # Save as CSV for easy reference
    reference_df.to_csv('/tmp/outputs/strategic_hts_codes_reference.csv', index=False)
    
    # Create summary table by category
    print("\n" + "="*80)
    print("STRATEGIC HTS CODES SUMMARY")
    print("="*80)
    
    for category, info in strategic_codes.items():
        print(f"\n🔹 {category}")
        print(f"   Impact: {info['trade_impact']}")
        print(f"   Dependency: {info['dependency_level']}")
        print(f"   Context: {info['description']}")
        print(f"   Key Codes: {len(info['codes'])} codes")
        
        # Show top 3 codes for each category
        print("   Priority Codes:")
        for i, (code, desc) in enumerate(list(info['codes'].items())[:3]):
            print(f"     • {code}: {desc}")
        if len(info['codes']) > 3:
            print(f"     ... and {len(info['codes'])-3} more")
    
    print(f"\n📊 Total Strategic HTS Codes: {len(reference_data)}")
    print(f"💾 Reference saved to: /tmp/outputs/strategic_hts_codes_reference.csv")

def main():
    """Generate comprehensive HTS code analysis guide."""
    
    print("🔍 STRATEGIC HTS CODES ANALYSIS")
    print("=" * 50)
    
    # Create HTS code definitions and reference
    create_hts_code_reference()
    
    # Create priority visualization
    print("\n📈 Creating priority matrix visualization...")
    create_hts_priority_matrix()
    
    # Create implementation guide  
    print("\n📋 Generating implementation guide...")
    create_implementation_guide()
    
    print("\n✅ HTS ANALYSIS COMPLETE")
    print("\n📊 Files Generated:")
    print("   • strategic_hts_codes_reference.csv")
    print("   • strategic_hts_priority_matrix.png")
    print("   • hts_implementation_guide.md")

if __name__ == "__main__":
    main()