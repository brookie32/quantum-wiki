---
title: "Dashboard"
---

# Quantum Wiki — Dashboard

## Recent entries

```dataview
TABLE date, category, source, summary
FROM ""
WHERE file.name != "index" AND file.name != "log" AND file.name != "overview"
SORT date DESC
LIMIT 20
```

## Agent entries (last 7 days)

```dataview
TABLE date, category, summary
FROM ""
WHERE source = "agent"
SORT date DESC
LIMIT 10
```

## Stale entries

```dataview
TABLE date, review_by, category
FROM ""
WHERE stale = true
SORT review_by ASC
```


## Related
- [[index|Quantum Wiki Index]]
- [[log|Activity Log]]
- [[overview|Quantum Wiki Overview]]
