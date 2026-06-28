# for silver.person
# contains match
# MainBranch
MainBranch_RULES = [
    ("am a developer", "Professional Developer"),
    ("not primarily a developer", "Occasional Developer"),
    ("used to be a developer", "Former Developer"),
    ("am learning", "Learner"),
    ("am a student", "Student"),
    ("as a hobby", "Hobbyist"),
    ("supports developers", "Support Developer"),
    ("None of these", "Other"),
]

# Edlevel
Edlevel_RULES = [
    ("Primary", "Primary School"),
    ("Secondary", "Secondary School "),
    ("Some college", "Some College"),
    ("Associate", "Associate Degree"),
    ("Bachelor", "Bachelor’s Degree"),
    ("Master", "Master’s Degree"),
    ("Professional", "Doctoral/Professional Degree"),
    ("doctoral", "Doctoral/Professional Degree"),  
    ("Something else", "Other"),
]

# DevType
DevType_RULES = [
    ("Developer", "Engineering / Dev"),

    ("Data scientist", "Data / AI"),
    ("Data engineer", "Data / AI"),
    ("Engineer, data", "Data / AI"),
    ("AI/ML engineer", "Data / AI"),
    ("Applied scientist", "Data / AI"),
    ("Scientist", "Data / AI"),
    ("Data or business analyst", "Data / AI"),

    ("DevOps", "Infra / DevOps"),
    ("System administrator", "Infra / DevOps"),
    ("Cloud infrastructure", "Infra / DevOps"),
    ("site reliability", "Infra / DevOps"),

    ("Security", "Security"),
    ("Cybersecurity", "Security"),

    ("Designer", "Design"),
    ("UX", "Design"),

    ("manager", "Management"),
    ("executive", "Management"),
    ("Founder", "Management"),

    ("Research", "Research"),
    ("Educator", "Education"),
    ("Student", "Student"),
]

# RemoteWork
RemoteWork_RULES = [
    ("Remote", "Remote"),
    ("In-person", "On-site"),
    ("Hybrid", "Hybrid"),
    ("Your choice", "Flexible"),
]

# PurchaseInfluence
PurchaseInfluence_RULES = [
    ("substantial addition", "High Influence"),
    ("great deal of influence", "High Influence"),
    ("more than five colleagues", "Medium Influence"),
    ("some influence", "Medium Influence"),
    ("more than just myself", "Medium Influence"),
    ("ultimately not purchased", "Low Influence"),
    ("little or no influence", "Low Influence"),
    ("No", "None"),
]

# NewRole
NewRole_RULES = [
    ("strongly considered", "Strongly Considered"),
    ("somewhat considered", "Considered"),
    ("voluntarily", "Voluntary"),
    ("involuntarily", "Involuntary"),
    ("neither consider", "Not Considering"),
]

# AISelect
AISelect_RULES = [
    ("daily", "Daily"),
    ("weekly", "Weekly"),
    ("monthly or infrequently", "Occasional"),
    ("plan to soon", "Planning"),
    ("don't plan to", "None"),
]

# AISent
AISent_RULES = [
    ("Very favorable", "Very Favorable"),
    ("Favorable", "Favorable"),
    ("Indifferent", "Neutral"),
    ("Unfavorable", "Unfavorable"),
    ("Very unfavorable", "Very Unfavorable"),
    ("Unsure", "Unsure"),
]

# AIAcc
AIAcc_RULES = [
    ("Highly trust", "High Trust"),
    ("Somewhat trust", "Trust"),
    ("Neither trust nor distrust", "Neutral"),
    ("Somewhat distrust", "Distrust"),
    ("Highly distrust", "High Distrust"),
]

# exact match
# Age
Age_RULES = [
    ("Younger than 5 years", "Under 18"),
    ("5 - 10 years", "Under 18"),
    ("11 - 17 years", "Under 18"),
    ("Under 18 years old", "Under 18"),
    ("18-24 years old", "18-24"),
    ("25-34 years old", "25-34"),
    ("35-44 years old", "35-44"),
    ("45-54 years old", "45-54"),
    ("55-64 years old", "55-64"),
    ("65 years or older", "65+"),
    ("Prefer not to say", "Unknown"),
]

# Industry
Industry_RULES = [
    ("Banking/Financial Services", "Financial Services"),
    ("Financial Services", "Financial Services"),
    ("Fintech", "Financial Services"),
    ("Insurance", "Financial Services"),
    ("Software Development", "Technology"),
    ("Information Services, IT, Software Development, or other Technology", "Technology"),
    ("Computer Systems Design and Services", "Technology"),
    ("Internet, Telecomm or Information Services", "Technology"),
    ("Healthcare", "Healthcare"),
    ("Higher Education", "Education"),
    ("Government", "Public Sector"),
    ("Manufacturing, Transportation, or Supply Chain", "Manufacturing & Logistics"),
    ("Transportation, or Supply Chain", "Manufacturing & Logistics"),
    ("Manufacturing", "Manufacturing & Logistics"),
    ("Retail and Consumer Services", "Retail & Consumer"),
    ("Wholesale", "Retail & Consumer"),
    ("Energy", "Energy"),
    ("Oil & Gas", "Energy"),
    ("Legal Services", "Professional Services"),
    ("Advertising Services", "Media & Advertising"),
    ("Media & Advertising Services", "Media & Advertising"),
    ("Other", "Other"),
]

# OrgSize
OrgSize_RULES = [
    ("Just me", "Self-Employed"),
    ("2 to 9 employees", "<20"),
    ("10 to 19 employees", "<20"),
    ("Less than 20 employees", "20 to 99"),
    ("100 to 499 employees", "100 to 499"),
    ("500 to 999 employees", "500 to 999"),
    ("1,000 to 4,999 employees", "1000 to 4999"),
    ("5,000 to 9,999 employees", "5000 to 9999"),
    ("10,000 or more employees", ">=10000"),
    ("I don’t know", "Unknown"),
]

# startswith
# Employment
Employment_RULES = [
    ("Employed", "Employed"),
    ("Independent contractor", "Self-Employed"),
    ("Student", "Student"),
    ("Not employed", "Not employed"),
    ("Retired", "Retired"),
]