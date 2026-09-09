```mermaid

erDiagram
    REPOSITORIES ||--o{ WORKFLOW_FILES : "posee"
    WORKFLOW_FILES ||--|| WORKFLOW_METADATA : "tiene"

    REPOSITORIES {
        int repository_id PK
        string owner
        string name
        string full_name
    }

    WORKFLOW_FILES {
        string file_id PK
        int repository_id FK
        string file_name
        string file_path
        string body_markdown
    }

    WORKFLOW_METADATA {
        string metadata_id PK
        string file_id FK
        string name
        string description
        string tools
        string raw_frontmatter_json
    }
