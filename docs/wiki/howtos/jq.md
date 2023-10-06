---
tags:
  - jq
  - json
---

# jq

## References

- ["Reshaping JSON with jq" by Matthew Lincoln](https://programminghistorian.org/en/lessons/json-and-jq)

## Get Kubernetes pods labels and store them in CSV format

- Get pods in JSON format

```shell
$ kubectl get pods -team=my-team-name -o json > pods.json
```

??? example "Example `pods.json`"

    ```json
    {
        "items": [
            {
                "metadata": {
                    "labels": {
                        "application": "app_X",
                        "component": "compo_A"
                    },
                    "name": "some_name_1"
                }
            },
            {
                "metadata": {
                    "labels": {
                        "application": "app_Y"
                    },
                    "name": "some_name_2"
                }
            },
            {
                "metadata": {
                    "labels": {
                        "application": "app_Z",
                        "component": "compo_B"
                    },
                    "name": "some_name_3"
                }
            }
        ],
        "kind": "List",
        "metadata": {
            "resourceVersion": "",
            "selfLink": ""
        }
    }
    ```

- `jq` generates CSV with header
  - CSV header: `["application", "pod_name", "component"]` 
  - default value if value is null: `.labels.component // "N/A"`

```shell
cat pods.json |\
jq -r '["application", "pod_name", "component"], 
(.items[].metadata | [.labels.application, .name, .labels.component // "N/A"]) 
| @csv'
```

!!! note "output.csv"

    ```csv
    "application","pod_name","component"
    "app_X","some_name_1","compo_A"
    "app_Y","some_name_2","N/A"
    "app_Z","some_name_3","compo_B"
    ```
