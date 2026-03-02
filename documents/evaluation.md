# Week 10 Evaluation: CodeReview / PR

**Authors:** [Neel Sanjaybhai Faganiya, Ibrahim Mohammed Sayem, Felix Wang]


## 1. Evaluation Criteria

This section defines how students can determine whether they solved the example problems correctly.

Criteria should be applicable to any problem in this topic.

* Criteria 1
* Criteria 2
* Criteria n

---

## 2. Evalation specifically for Example Problems

### Problem A_1: [Title]

**Evaluation Description:**  
Describe the evaluation criteria clearly and precisely.

**Code:**  
// Include all necessary code here that is the correct answer.

---

### Problem A_2: [Title]

**Evaluation Description:**  
Describe the evaluation criteria clearly and precisely.

**Code:**  
// Include all necessary code here that is the correct answer.

---

### Problem A_n: [Title]

**Evaluation Description:**  
Describe the evaluation criteria clearly and precisely.

**Code:**  
// Include all necessary code here that is the correct answer.

---

### Problem C: Pull Request Supply Chain Review

**Evaluation Description:**  
This problem will not likely be resolved by simply letting LLMs inspect the dependency files before and after PR. LLMs are not designed to reliably reason over large, highly-structured lockfile. A reasonable process is to apply dependency management tools like Dependabot and/or dependency-review-action@v4 for identifying vulnerable packages. 
In this PR, the package "multer": "2.1.0" is changed to "multer": "2.0.2". 

However, multer package versions < 2.1.0 are known to be severely vulnerable to Denial of Service attacks (CVE-2026-3304). More details can be found on the National Vulnerability Database (NVD)'s official website [https://nvd.nist.gov/vuln/detail/CVE-2026-3304](https://nvd.nist.gov/vuln/detail/CVE-2026-3304), and from the table below:

|             | CVE-2026-3304           |
|-------------|-------------------------------------|
| Severity   | High |
| CVSS Score | 8.7 |
|  Description  | Multer is a node.js middleware for handling `multipart/form-data`. A vulnerability in Multer prior to version 2.1.0 allows an attacker to trigger a Denial of Service (DoS) by sending malformed requests, potentially causing resource exhaustion. Users should upgrade to version 2.1.0 to receive a patch. No known workarounds are available.                                    |
| NVD Published Date | 02/27/2026 |
| Attack Vector | Network |
| Attack Complexity | Low |
| Attack Requirement | None |
| Privileges Required | None | 
| User Interaction | None |
| Related CWE | CWE-459: Incomplete Cleanup | 

Any approach that successfully identified this vulnerable dependency is a correct solution. 

---

### Problem D: Northwind Signal Project PR Review

#### Problem D.1: Usage Audit Feature PR Review

**Evaluation Description:**

The most severe issue contained in this PR is that, the binary executable file under the folder `problem_d/problem_d_backend/src/vendor` called `audit_writer` is simulating some malicious behaviours. Don't worry though, it's not really malicious, you can find the file in the `audit_writer-file` branch. All it does is to create a data record with a message: `This is a malicious event in the binary file, your database is now compromised`. However, the real security concern is not the message itself. The core issue is that: A precompiled binary executable has been committed directly into the repository and invoked by backend logic!

Any PR review comments questioning the necessity of doing so, asking for cryptographic evidence, and ways to reproduce it is a good solution. 

There are other severe issues in this PR, your solution is good if you find more or all of them: 
```
1. Missing Type Safety on Event Handler
File: main.ts
Lines: ~382-395
Issue: The auditButton might be null, but the code proceeds without proper guards in some places.

2. Implicit any Type on Error
File: main.ts, usage.service.ts
Lines: ~364-365 and ~393-394, ~46-50
Issue: Bare catch blocks without typing violate the TypeScript standard of avoiding any types.

3. Insufficient Input Validation
File: main.ts
Lines: ~384-388
Issue: No validation of the API response before rendering. The entries array could be malformed.

4. Arbitrary Command Execution Vulnerability
File: usage.service.ts
Lines: ~32-40
Issue: Using execFile with unsanitized user input (message) as a command argument.
Risk: Although execFile is safer than exec, the message parameter should be further validated/sanitized.

5. Missing Input Validation: Message Length Enforcement
File: usage.controller.ts
Lines: ~12-17
Issue: Message length limit (1000 chars) is enforced but could be externalized as a constant.
Recommendation: Create a constants file with validation rules.

6. There are no tests
No unit tests for usage.service.ts (following TypeScript standard that requires unit tests for all exported functions)
No integration tests for the new endpoints (GET /usage/audit-log, POST /usage/audit)
No frontend tests for the new audit panel UI and event handlers
```

#### Problem D.2: Annual Report Generation PR Review

**Evaluation Description:**
TypeScript is a superset of JavaScript, and it adds static typing and compile-time checks on top of JavaScript, which offers compile-time guarantees, early error detection, and safer refactoring. Therefore, when TypeScript developers bypass the type system by abusing the `any` type, it could cause the guarantee provided by TS collapse to JS-level safety. That undermines the primary reason for choosing TypeScript in the first place. 

And there are other naming conventions in TypeScript like using `camelCase` for variables and functions, and use `PascalCase` for class and interface names. This is for better consistency, readibility and maintainability across the codebase. 

**Criteria 1:** Your solution is good if you catch more or all `any` type abuses:

| # | File Name |   Line Number       | Code Snippet         |
|---|--|--------|-------------------------------------|
| 1 |problem_d/problem_d_backend/src/modules/reports/reports.controller.ts | 10 | `const resolvedYear: any = year ? Number(year) : new Date().getFullYear() - 1;`| 
| 2 |problem_d/problem_d_backend/src/modules/reports/reports.controller.ts | 11 | `const orgId: any = organizationId ?? 'org_001';`|
| 3 |problem_d/problem_d_backend/src/modules/reports/reports.service.ts | 8 | `CompanyReport(organizationId: any, year: any): any {)`|
| 4 |problem_d/problem_d_backend/src/modules/reports/reports.service.ts | 9 | `const org: any = this.db.get()`|
| 5 |problem_d/problem_d_backend/src/modules/reports/reports.service.ts | 22 | ``const startDate: any = `${year}-01-01`;``|
| 6 |problem_d/problem_d_backend/src/modules/reports/reports.service.ts | 23 | ``const EndDate: any = `${year}-12-31`;``|
| 7 |problem_d/problem_d_backend/src/modules/reports/reports.service.ts | 25 | ``const invoiceSummary: any = this.db.get()``|
| 8 |problem_d/problem_d_backend/src/modules/reports/reports.service.ts | 35 | ``const projectSummary: any = this.db.get()``|
| 9 |problem_d/problem_d_backend/src/modules/reports/reports.service.ts | 43 | ``const lastProject: any = this.db.get()``|
| 10 |problem_d/problem_d_backend/src/modules/reports/reports.service.ts | 52 | ``const usage: any = this.db.get()``|
| 11 |problem_d/problem_d_backend/src/modules/reports/reports.service.ts | 61 | ``const summaryPoints: any[] = []``|
| 12 |problem_d/problem_d_backend/src/modules/reports/reports.service.ts | 69 | ``const keyMetrics: any[] = []``|
| 13 |problem_d/problem_d_backend/src/modules/reports/reports.service.ts | 76 | ``const narrative: any =``|
| 14 |problem_d/problem_d_backend/src/modules/reports/reports.service.ts | 80 | ``const ReportData: any = {``|
| 15 |problem_d/problem_d_frontend/src/main.ts | 288 | ``const RenderReport = (payload: any) => {``|
| 16 |problem_d/problem_d_frontend/src/main.ts | 306 | ``(metric: any) => ``|
| 17 |problem_d/problem_d_frontend/src/main.ts | 315 | ``map((item: any) => `<li>${item}</li>`).join('')}``|
| 18 |problem_d/problem_d_frontend/src/main.ts | 321 | ``const lastYear: any = new Date().getFullYear() - 1;``|
| 19 |problem_d/problem_d_frontend/src/main.ts | 322 | ``const reportButton: any = document.getElementById``|
| 20 |problem_d/problem_d_frontend/src/main.ts | 323 | ``const ReportYear: any = document.getElementById()``|
| 21 |problem_d/problem_d_frontend/src/main.ts | 324 | ``const reportStatus: any = document.getElementById()``|
| 22 |problem_d/problem_d_frontend/src/main.ts | 326 | ``let ReportData: any = null;``|
| 23 |problem_d/problem_d_frontend/src/main.ts | 327 | ``const setreportData: any = (value: any) => {``|
| 24 |problem_d/problem_d_frontend/src/main.ts | 344 | ``const res: any = await fetch``|
| 25 |problem_d/problem_d_frontend/src/main.ts | 345 | ``const data: any = await res.json();``|
| 26 |problem_d/problem_d_frontend/src/main.ts | 350 | ``} catch (error: any) {``|

Try to think about:
- Did the LLM-assisted PR review tool catch all these? Why or why not?
- The static analysis tool only caught 21, why do you think this happened (See PR #11 -> Files changed)?

**Criteria 2:** And your solution is good if you catch more or all naming convention violations:

| # | File Name |   Line Number       | Code Snippet         |
|---|--|--------|-------------------------------------|
| 1 |problem_d/problem_d_backend/src/modules/reports/reports.service.ts | 23 | ``const EndDate: any = `${year}-12-31`;``|
| 2 |problem_d/problem_d_backend/src/modules/reports/reports.service.ts | 8 | ``CompanyReport(organizationId: any, year: any): any {``|
| 3 |problem_d/problem_d_backend/src/modules/reports/reports.service.ts | 80 | ``const ReportData: any = {``|
| 4 |problem_d/problem_d_frontend/src/main.ts | 288 | ``const RenderReport = (payload: any) => {``|
| 5 |problem_d/problem_d_frontend/src/main.ts | 320 | ``const LoadReport = (): any => {``|
| 6 |problem_d/problem_d_frontend/src/main.ts | 323 | ``const ReportYear: any = document.getElementById(``|
| 7 |problem_d/problem_d_frontend/src/main.ts | 326 | ``let ReportData: any = null;``|

Try to think about:
- Did the LLM-assisted PR review tool catch all these? Why or why not?

**Criteria 3:** Your solution is good if you catch that the test cases for this PR will not pass. 

The test case at line 54 of the file `problem_d/problem_d_backend/src/modules/reports/reports.service.spec.ts` will not pass: `expect(result.year).toBe(2026);`. 










## 3. References

[1]  
[2] 

---

