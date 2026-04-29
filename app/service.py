from app.neo4j import driver
from app.calendar import create_calendar_event

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
        session.run(query, **data.dict())

    create_calendar_event(data)

    return f"Delivery created for {data.customer_name}"

