# Neo4j - Graph Database

## Overview

Neo4j is a powerful graph database designed for storing and querying highly connected data. It's ideal for knowledge graphs, recommendation systems, and modeling complex relationships in AI applications.

## Technical Configuration

### Storage
- **Data**: `data/neo4j/data/`
- **Logs**: `data/neo4j/logs/`
- **Config**: `config/neo4j.conf`

### Ports
- **HTTP**: `http://localhost:7474` (Browser UI)
- **Bolt**: `bolt://localhost:7687` (Database connection)

### Authentication
- **Username**: `neo4j`
- **Password**: `password123` (change in `.env`)

## How to Use Neo4j

### 1. Access Neo4j Browser
Open your browser:
```
http://localhost:7474
```

Login with:
- **Username**: `neo4j`
- **Password**: `password123`

### 2. Create Nodes and Relationships

#### Create Nodes
```cypher
CREATE (p:Person {name: "Alice", age: 30})
CREATE (c:Company {name: "TechCorp"})
RETURN p, c
```

#### Create Relationships
```cypher
MATCH (p:Person {name: "Alice"})
MATCH (c:Company {name: "TechCorp"})
CREATE (p)-[:WORKS_AT {since: 2020}]->(c)
RETURN p, c
```

### 3. Query Data

#### Find Nodes
```cypher
MATCH (p:Person)
WHERE p.age > 25
RETURN p
```

#### Find Relationships
```cypher
MATCH (p:Person)-[r:WORKS_AT]->(c:Company)
RETURN p.name, c.name, r.since
```

#### Path Queries
```cypher
MATCH path = (a:Person)-[:KNOWS*1..3]-(b:Person)
WHERE a.name = "Alice"
RETURN path
```

## Use Cases for AI Applications

### 1. Knowledge Graphs
Store entities and their relationships:
```cypher
CREATE (concept:Concept {name: "Machine Learning"})
CREATE (subconcept:Concept {name: "Neural Networks"})
CREATE (subconcept)-[:IS_A]->(concept)
```

### 2. Conversation Context
Track conversation flow and context:
```cypher
CREATE (user:User {id: "user123"})
CREATE (msg1:Message {text: "Hello", timestamp: datetime()})
CREATE (msg2:Message {text: "How are you?", timestamp: datetime()})
CREATE (user)-[:SENT]->(msg1)
CREATE (msg1)-[:FOLLOWED_BY]->(msg2)
```

### 3. Agent Relationships
Model multi-agent systems:
```cypher
CREATE (agent1:Agent {name: "Researcher", role: "research"})
CREATE (agent2:Agent {name: "Writer", role: "content"})
CREATE (agent1)-[:DELEGATES_TO]->(agent2)
```

## Integration with Other Services

### Python Integration
```python
from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "password123")
)

with driver.session() as session:
    result = session.run(
        "MATCH (p:Person) RETURN p.name AS name"
    )
    for record in result:
        print(record["name"])
```

### n8n Integration
Use HTTP Request node with Cypher queries:
```
URL: http://ai-neo4j:7474/db/neo4j/tx/commit
Method: POST
Headers: Authorization: Basic bmVvNGo6cGFzc3dvcmQxMjM=
Body: {
  "statements": [{
    "statement": "MATCH (n) RETURN n LIMIT 10"
  }]
}
```

### Langflow/Flowise Integration
Use custom Python components to query Neo4j.

## Advanced Features

### Indexes
Create indexes for faster queries:
```cypher
CREATE INDEX person_name FOR (p:Person) ON (p.name)
```

### Constraints
Ensure data integrity:
```cypher
CREATE CONSTRAINT person_id FOR (p:Person) REQUIRE p.id IS UNIQUE
```

### Full-Text Search
```cypher
CALL db.index.fulltext.createNodeIndex(
  "personNames",
  ["Person"],
  ["name"]
)

CALL db.index.fulltext.queryNodes("personNames", "Alice")
YIELD node
RETURN node
```

## Backup and Restore

### Export Data
```cypher
CALL apoc.export.json.all("backup.json", {})
```

### Backup Database
```bash
docker exec ai-neo4j neo4j-admin dump --database=neo4j --to=/backups/neo4j.dump
```

### Restore
```bash
docker exec ai-neo4j neo4j-admin load --from=/backups/neo4j.dump --database=neo4j --force
```

## Monitoring

### Database Info
```cypher
CALL dbms.components()
```

### Performance
```cypher
CALL dbms.queryJmx("org.neo4j:*")
```

## Troubleshooting

### Check Logs
```bash
docker logs ai-neo4j
cat data/neo4j/logs/neo4j.log
```

### Restart Neo4j
```bash
docker restart ai-neo4j
```

### Clear Database
```cypher
MATCH (n) DETACH DELETE n
```

## Resources

- [Official Documentation](https://neo4j.com/docs/)
- [Cypher Manual](https://neo4j.com/docs/cypher-manual/)
- [Graph Academy](https://graphacademy.neo4j.com/)
- [APOC Library](https://neo4j.com/labs/apoc/)
