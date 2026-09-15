# Test Strategy: [Product/Service]
## Author: [Name] | Date: [Date] | Scope: [System/Feature]
## 1. Quality Goals
| Goal | Metric | Target |
|:---|:---|:---|
| Reliability | Test pass rate | ≥99% |
| Coverage | Line coverage (unit) | ≥80% |
| Speed | CI pipeline duration | <15 min |
## 2. Test Pyramid
| Layer | Scope | Count Target | Tools | Responsibility |
|:---|:---|:---|:---|:---|
| **Unit** | Functions/classes | Majority (~70%) | [Jest/pytest/JUnit] | Developer |
| **Integration** | Component interactions | Moderate (~20%) | [Testcontainers] | Developer |
| **Contract** | API compatibility | Per consumer | [Pact] | Consumer team |
| **E2E** | Critical user journeys | Few (~10%) | [Playwright/Cypress] | QE team |
## 3. Specialized Testing
| Type | Scope | Frequency | Tools |
|:---|:---|:---|:---|
| Performance | Load/stress test | Per release | [k6/Gatling] |
| Security | SAST + DAST + SCA | Every CI run / weekly | [Snyk/SonarQube/ZAP] |
| Chaos | Failure injection | Monthly | [Gremlin/LitmusChaos] |
| Accessibility | WCAG 2.2 AA | Per release | [axe-core/Lighthouse] |
## 4. Test Environments
| Environment | Purpose | Data | Refresh |
|:---|:---|:---|:---|
| Local | Developer testing | Fixtures | N/A |
| CI | Automated pipeline | Synthetic | Per run |
| Staging | Pre-prod validation | Anonymized prod | Weekly |
## 5. Quality Gates
| Gate | Criteria | Blocking? |
|:---|:---|:---|
| PR merge | All unit+integration pass, coverage ≥80% | Yes |
| Deploy to staging | E2E pass, no P1 bugs | Yes |
| Deploy to prod | Canary metrics healthy 30min | Yes |
