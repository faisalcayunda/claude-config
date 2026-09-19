# Data Taxonomy: [Product Name]
## Version: [1.0] | Owner: [Name] | Date: [Date]
## Taxonomy Governance
| Role | Responsibility | Person |
|:---|:---|:---|
| Taxonomy Owner | Approve new events, enforce standards | [Name] |
| Implementer | Instrument events in code | [Eng team] |
| Consumer | Use data for analysis | [Analytics team] |
## Naming Standards
| Element | Convention | Example | Anti-pattern |
|:---|:---|:---|:---|
| Events | [Object] [Past-Tense Verb], Title Case | "Cart Updated" | "updateCart", "cart_update" |
| Event Properties | snake_case, descriptive | item_count | cnt, n |
| User Properties | snake_case, prefixed by domain | billing_plan_type | type |
## Event Categories
| Category | Events | Business Purpose |
|:---|:---|:---|
| Lifecycle | Session Started, Signed Up, Subscription Started | Funnel tracking |
| Core Actions | [Product-specific core actions] | Engagement & retention |
| Feature Usage | Feature Viewed, Feature Used | Adoption tracking |
| Revenue | Purchase Completed, Subscription Renewed | Revenue analytics |
## Property Standards
| Standard | Rule | Example |
|:---|:---|:---|
| IDs | Always string, prefixed | "item_abc123" |
| Amounts | Integer cents (not float dollars) | 1999 (= $19.99) |
| Dates | ISO 8601 UTC | "2024-03-15T10:30:00Z" |
| Booleans | is_ or has_ prefix | is_premium, has_completed |
