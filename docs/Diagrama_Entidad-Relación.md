```mermaid

erDiagram
    REPOSITORIES ||--o{ WORKFLOW_FILES : "posee"
    WORKFLOW_FILES ||--|| WORKFLOW_METADATA : "tiene"
    WORKFLOW_LOCK }o--|| WORKFLOW_FILES : "Asocia"

    REPOSITORIES {
        int repository_id 
        string owner
        string name
        string full_name
    }

    WORKFLOW_FILES {
        string file_id
        int repository_id 
        string file_name
        string file_path
        string body_markdown
    }

    WORKFLOW_METADATA {
        string metadata_id 
        string file_id 
        string name
        string description
        string tools
        string raw_frontmatter_json
    }
        
    WORKFLOW_LOCK {
        
    }