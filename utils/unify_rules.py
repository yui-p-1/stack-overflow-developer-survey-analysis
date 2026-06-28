# for silver.person_skill
# exact match
Language_RULES = [
    ("Bash/Shell", "Bash/Shell (all shells)"),
    ("Cobol", "COBOL"),
    ("LISP", "Lisp"),
    ("Matlab", "MATLAB"),
]

Database_RULES = [
    ("ClickHouse", "Clickhouse"),
    ("CockroachDB", "Cockroachdb"),
    ("CouchDB", "Couch DB"),
    ("DynamoDB", "Dynamodb"),
    ("Neo4j", "Neo4J"),
]

Platform_RULES = [
    ("AWS", "Amazon Web Services (AWS)"),  
    ("DigitalOcean", "Digital Ocean"),
    ("Google Cloud Platform", "Google Cloud"),
    ("IBM Cloud", "IBM Cloud or Watson"),
    ("IBM Cloud Or Watson", "IBM Cloud or Watson"),
    ("Linode", "Linode, now Akamai"),   
    ("Oracle Cloud Infrastructure", "Oracle Cloud Infrastructure (OCI)"),
]

Webframe_RULES = [
    ("Angular.js", "AngularJS"),  
    ("React.js", "React"),
    ("ASP.NET CORE", "ASP.NET Core"),
]

OpSys_RULES = [
    ("Other (please specify):", "Other (Please Specify):"),
    ("macOS", "MacOS"),
    ("Linux-based", "Linux (non-WSL)"),
    ("Other Linux-based", "Linux (non-WSL)"),
]