from neo4j import GraphDatabase

# Replace these with your actual Neo4j credentials
URI = "bolt://localhost:7687"
AUTH = ("neo4j", "your_password")

# Initialize the driver
driver = GraphDatabase.driver(URI, auth=AUTH)

def create_delivery(data):
    query = """
    MERGE (c:Customer {code: $customer_code})
      ON CREATE SET c.name = $customer_name
        
    CREATE (e:Delivery {
        date: $delivery_date,
        items: $items,
        vehicle: $vehicle_type,
        address: $delivery_address,
        attn: $attn_name,
        attnNum: $attn_num,
        itemCode: $itemCode,
        timestamp: datetime()
    })
    CREATE (e)-[:TO_CUSTOMER]->(c)
    """

    with driver.session() as session:
        # Note: Using .dict() works for Pydantic v1. 
        # For Pydantic v2, use .model_dump()
        session.run(query, **data.dict())

    return f"Delivery created for {data.customer_name}"