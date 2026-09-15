# API Design Document: [API Name]
## Author: [Name] | Date: [Date] | Version: [v1.0]
## 1. Overview
[What this API does, who uses it, key constraints]
## 2. Design Principles
- Consumer-first (designed for DX, not internal model)
- Consistent naming and error handling
- Versioned (URL path: /v1/)
- Idempotent where applicable
## 3. Authentication & Authorization
| Method | Scope |
|:---|:---|
| [OAuth 2.0 / API Key / JWT] | [Who can access what] |
## 4. Endpoints
### [Resource]: /api/v1/[resources]
| Method | Path | Description | Auth |
|:---|:---|:---|:---|
| GET | /resources | List resources (paginated) | [Scope] |
| POST | /resources | Create resource | [Scope] |
| GET | /resources/{id} | Get resource by ID | [Scope] |
| PUT | /resources/{id} | Update resource | [Scope] |
| DELETE | /resources/{id} | Delete resource | [Scope] |
### Request/Response Examples
[Example request body + response body for key operations]
## 5. Error Handling
| Status | Code | Message | When |
|:---|:---|:---|:---|
| 400 | INVALID_INPUT | [Field-level errors] | Validation failure |
| 401 | UNAUTHORIZED | [Auth error] | Missing/invalid token |
| 404 | NOT_FOUND | [Resource not found] | Invalid ID |
| 429 | RATE_LIMITED | [Retry-After header] | Exceeded rate limit |
## 6. Pagination
[Cursor-based / Offset-based with standard parameters]
## 7. Rate Limiting
[Limits per tier, Retry-After headers, burst allowance]
## 8. OpenAPI Specification
[Link to generated OpenAPI YAML/JSON]
