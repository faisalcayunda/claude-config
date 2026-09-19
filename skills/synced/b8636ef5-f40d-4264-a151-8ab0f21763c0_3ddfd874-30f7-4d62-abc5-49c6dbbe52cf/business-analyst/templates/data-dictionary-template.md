# Data Dictionary: [System/Module Name]
## Version: [1.0] | Author: [Name] | Date: [Date]
## Entities
| Entity | Description | Owner | Source System |
|:---|:---|:---|:---|
## Data Elements
| Entity | Element | Definition | Data Type | Length | Required | Valid Values | Business Rule | Source |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| [Customer] | customer_id | Unique customer identifier | UUID | 36 | Yes | System-generated | Auto-increment | [System] |
| [Customer] | email | Primary contact email | VARCHAR | 255 | Yes | Valid email format | BRL-001: unique per customer | [Registration] |
## Relationships
| Parent Entity | Child Entity | Cardinality | FK Field |
|:---|:---|:---|:---|
| Customer | Order | 1:M | customer_id |
