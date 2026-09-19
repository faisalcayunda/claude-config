# Tracking Plan: [Product Name]
## Version: [1.0] | Author: [Name] | Date: [Date]
## Naming Convention
**Events**: [Object] + [Past-Tense Verb], Title Case (e.g., "Article Viewed")
**Properties**: snake_case (e.g., article_id, category)
## Core Events
| Event Name | Description | Trigger | Key Properties | Platform | Source | Priority |
|:---|:---|:---|:---|:---|:---|:---|
| Session Started | User opens app/site | App launch / page load | session_id, referrer, utm_source | All | Client | Must |
| [Object] [Verb] | [Business meaning] | [When it fires] | [property: type] | [Web/iOS/Android] | [Client/Server] | Must/Should/Could |
## User Properties
| Property | Type | Description | Source | Example |
|:---|:---|:---|:---|:---|
| user_id | string | Unique user identifier | Auth system | "usr_abc123" |
| plan_type | string | Current subscription tier | Billing | "pro" |
| signup_date | datetime | Account creation date | Registration | "2024-01-15" |
## Identity Resolution Strategy
| Identifier | Type | When Set | Merge Rule |
|:---|:---|:---|:---|
| anonymous_id | UUID | First visit (cookie/device) | Merge to user_id on login |
| user_id | string | On authentication | Primary identifier |
## Implementation Status
| Event | Spec'd | Dev'd | QA'd | Live | Notes |
|:---|:---|:---|:---|:---|:---|
