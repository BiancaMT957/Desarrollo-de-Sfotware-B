

### Adapter

```
bianca007@MSI:/mnt/c/Users/Bianca/Documents/Laboratorio7/Adapter$ python main.py
Command 'python' not found, did you mean:
  command 'python3' from deb python3
  command 'python' from deb python-is-python3
bianca007@MSI:/mnt/c/Users/Bianca/Documents/Laboratorio7/Adapter$ python3 main.py
bianca007@MSI:/mnt/c/Users/Bianca/Documents/Laboratorio7/Adapter$ terraform init
Initializing the backend...
Initializing provider plugins...
- Finding latest version of hashicorp/null...
- Installing hashicorp/null v3.2.4...
- Installed hashicorp/null v3.2.4 (signed by HashiCorp)
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
bianca007@MSI:/mnt/c/Users/Bianca/Documents/Laboratorio7/Adapter$ terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the     
following symbols:
  + create

Terraform will perform the following actions:

  # null_resource.identity_audit_team_read will be created
  + resource "null_resource" "identity_audit_team_read" {
      + id       = (known after apply)
      + triggers = {
          + "identity" = "audit-team"
          + "role"     = "read"
          + "user"     = "audit-team"
        }
    }

  # null_resource.identity_automation_01_write will be created
  + resource "null_resource" "identity_automation_01_write" {
      + id       = (known after apply)
      + triggers = {
          + "identity" = "automation-01"
          + "role"     = "write"
          + "user"     = "automation-01"
        }
    }

  # null_resource.identity_infrastructure_team_write will be created
  + resource "null_resource" "identity_infrastructure_team_write" {
      + id       = (known after apply)
      + triggers = {
          + "identity" = "infrastructure-team"
          + "role"     = "write"
          + "user"     = "infrastructure-team"
        }
    }

  # null_resource.identity_manager_team_admin will be created
  + resource "null_resource" "identity_manager_team_admin" {
      + id       = (known after apply)
      + triggers = {
          + "identity" = "manager-team"
          + "role"     = "admin"
          + "user"     = "manager-team"
        }
    }

  # null_resource.identity_user_01_read will be created
  + resource "null_resource" "identity_user_01_read" {
      + id       = (known after apply)
      + triggers = {
          + "identity" = "user-01"
          + "role"     = "read"
          + "user"     = "user-01"
        }
    }

  # null_resource.identity_user_02_read will be created
  + resource "null_resource" "identity_user_02_read" {
      + id       = (known after apply)
      + triggers = {
          + "identity" = "user-02"
          + "role"     = "read"
          + "user"     = "user-02"
        }
    }

  # null_resource.identity_user_03_write will be created
  + resource "null_resource" "identity_user_03_write" {
      + id       = (known after apply)
      + triggers = {
          + "identity" = "user-03"
          + "role"     = "write"
          + "user"     = "user-03"
        }
    }

Plan: 7 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

null_resource.identity_user_03_write: Creating...
null_resource.identity_user_01_read: Creating...
null_resource.identity_audit_team_read: Creating...
null_resource.identity_user_02_read: Creating...
null_resource.identity_manager_team_admin: Creating...
null_resource.identity_infrastructure_team_write: Creating...
null_resource.identity_automation_01_write: Creating...
null_resource.identity_infrastructure_team_write: Creation complete after 0s [id=7146361908792950001]
null_resource.identity_user_01_read: Creation complete after 0s [id=7518365789625124406]
null_resource.identity_audit_team_read: Creation complete after 0s [id=8649869468102814413]
null_resource.identity_user_03_write: Creation complete after 0s [id=3584964399514364746]
null_resource.identity_manager_team_admin: Creation complete after 0s [id=2437225068661704735]
null_resource.identity_user_02_read: Creation complete after 0s [id=3399756014275257018]
null_resource.identity_automation_01_write: Creation complete after 0s [id=2678127002385440232]

Apply complete! Resources: 7 added, 0 changed, 0 destroyed.
bianca007@MSI:/mnt/c/Users/Bianca/Documents/Laboratorio7/Adapter$ terraform destroy -auto-approve
null_resource.identity_automation_01_write: Refreshing state... [id=2678127002385440232]
null_resource.identity_user_01_read: Refreshing state... [id=7518365789625124406]
null_resource.identity_user_03_write: Refreshing state... [id=3584964399514364746]
null_resource.identity_audit_team_read: Refreshing state... [id=8649869468102814413]
null_resource.identity_manager_team_admin: Refreshing state... [id=2437225068661704735]
null_resource.identity_infrastructure_team_write: Refreshing state... [id=7146361908792950001]
null_resource.identity_user_02_read: Refreshing state... [id=3399756014275257018]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  - destroy

Terraform will perform the following actions:

  # null_resource.identity_audit_team_read will be destroyed
  - resource "null_resource" "identity_audit_team_read" {
      - id       = "8649869468102814413" -> null
      - triggers = {
          - "identity" = "audit-team"
          - "role"     = "read"
          - "user"     = "audit-team"
        } -> null
    }

  # null_resource.identity_automation_01_write will be destroyed
  - resource "null_resource" "identity_automation_01_write" {
      - id       = "2678127002385440232" -> null
      - triggers = {
          - "identity" = "automation-01"
          - "role"     = "write"
          - "user"     = "automation-01"
        } -> null
    }

  # null_resource.identity_infrastructure_team_write will be destroyed
  - resource "null_resource" "identity_infrastructure_team_write" {
      - id       = "7146361908792950001" -> null
      - triggers = {
          - "identity" = "infrastructure-team"
          - "role"     = "write"
          - "user"     = "infrastructure-team"
        } -> null
    }

  # null_resource.identity_manager_team_admin will be destroyed
  - resource "null_resource" "identity_manager_team_admin" {
      - id       = "2437225068661704735" -> null
      - triggers = {
          - "identity" = "manager-team"
          - "role"     = "admin"
          - "user"     = "manager-team"
        } -> null
    }

  # null_resource.identity_user_01_read will be destroyed
  - resource "null_resource" "identity_user_01_read" {
      - id       = "7518365789625124406" -> null
      - triggers = {
          - "identity" = "user-01"
          - "role"     = "read"
          - "user"     = "user-01"
        } -> null
    }

  # null_resource.identity_user_02_read will be destroyed
  - resource "null_resource" "identity_user_02_read" {
      - id       = "3399756014275257018" -> null
      - triggers = {
          - "identity" = "user-02"
          - "role"     = "read"
          - "user"     = "user-02"
        } -> null
    }

  # null_resource.identity_user_03_write will be destroyed
  - resource "null_resource" "identity_user_03_write" {
      - id       = "3584964399514364746" -> null
      - triggers = {
          - "identity" = "user-03"
          - "role"     = "write"
          - "user"     = "user-03"
        } -> null
    }

Plan: 0 to add, 0 to change, 7 to destroy.
null_resource.identity_infrastructure_team_write: Destroying... [id=7146361908792950001]
null_resource.identity_user_02_read: Destroying... [id=3399756014275257018]
null_resource.identity_user_03_write: Destroying... [id=3584964399514364746]
null_resource.identity_automation_01_write: Destroying... [id=2678127002385440232]
null_resource.identity_manager_team_admin: Destroying... [id=2437225068661704735]
null_resource.identity_audit_team_read: Destroying... [id=8649869468102814413]
null_resource.identity_user_01_read: Destroying... [id=7518365789625124406]
null_resource.identity_infrastructure_team_write: Destruction complete after 0s
null_resource.identity_user_01_read: Destruction complete after 0s
null_resource.identity_user_03_write: Destruction complete after 0s
null_resource.identity_audit_team_read: Destruction complete after 0s
null_resource.identity_manager_team_admin: Destruction complete after 0s
null_resource.identity_automation_01_write: Destruction complete after 0s
null_resource.identity_user_02_read: Destruction complete after 0s

Destroy complete! Resources: 7 destroyed.
bianca007@MSI:/mnt/c/Users/Bianca/Documents/Laboratorio7/Adapter$ cd ..
```


### Facade 

```
bianca007@MSI:/mnt/c/Users/Bianca/Documents/Laboratorio7$ cd Facade
bianca007@MSI:/mnt/c/Users/Bianca/Documents/Laboratorio7/Facade$ python main.py
Command 'python' not found, did you mean:
  command 'python3' from deb python3
  command 'python' from deb python-is-python3
bianca007@MSI:/mnt/c/Users/Bianca/Documents/Laboratorio7/Facade$ python3 main.py
bianca007@MSI:/mnt/c/Users/Bianca/Documents/Laboratorio7/Facade$ terraform init
Initializing the backend...
Initializing provider plugins...
- Finding hashicorp/null versions matching "~> 3.2"...
- Installing hashicorp/null v3.2.4...
- Installed hashicorp/null v3.2.4 (signed by HashiCorp)
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
bianca007@MSI:/mnt/c/Users/Bianca/Documents/Laboratorio7/Facade$ terraform apply -auto-approve

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  + create

Terraform will perform the following actions:

  # null_resource.bucket_access will be created
  + resource "null_resource" "bucket_access" {
      + id       = (known after apply)
      + triggers = {
          + "bucket" = "hello-world-storage-bucket"
          + "entity" = "allAuthenticatedUsers"
          + "role"   = "READER"
        }
    }

  # null_resource.storage_bucket will be created
  + resource "null_resource" "storage_bucket" {
      + id       = (known after apply)
      + triggers = {
          + "name" = "hello-world-storage-bucket"
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.
null_resource.storage_bucket: Creating...
null_resource.storage_bucket: Provisioning with 'local-exec'...
null_resource.storage_bucket (local-exec): Executing: ["python" "-c" "import pathlib; pathlib.Path(r'./buckets/hello-world-storage-bucket').mkdir(parents=True, exist_ok=True)"]
╷
│ Error: local-exec provisioner error
│
│   with null_resource.storage_bucket,
│   on bucket.tf.json line 16, in resource.null_resource.storage_bucket.provisioner[0].local-exec:
│   16:             }
│
│ Error running command 'import pathlib; pathlib.Path(r'./buckets/hello-world-storage-bucket').mkdir(parents=True,
│ exist_ok=True)': exec: "python": executable file not found in $PATH. Output:
╵
bianca007@MSI:/mnt/c/Users/Bianca/Documents/Laboratorio7/Facade$ terraform apply
null_resource.storage_bucket: Refreshing state... [id=7756975832935757617]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  + create
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # null_resource.bucket_access will be created
  + resource "null_resource" "bucket_access" {
      + id       = (known after apply)
      + triggers = {
          + "bucket" = "hello-world-storage-bucket"
          + "entity" = "allAuthenticatedUsers"
          + "role"   = "READER"
        }
    }

  # null_resource.storage_bucket is tainted, so must be replaced
-/+ resource "null_resource" "storage_bucket" {
      ~ id       = "7756975832935757617" -> (known after apply)
        # (1 unchanged attribute hidden)
    }

Plan: 2 to add, 0 to change, 1 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

null_resource.storage_bucket: Destroying... [id=7756975832935757617]
null_resource.storage_bucket: Destruction complete after 0s
null_resource.storage_bucket: Creating...
  # null_resource.storage_bucket is tainted, so must be replaced
-/+ resource "null_resource" "storage_bucket" {
      ~ id       = "7756975832935757617" -> (known after apply)
        # (1 unchanged attribute hidden)
    }

Plan: 2 to add, 0 to change, 1 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

null_resource.storage_bucket: Destroying... [id=7756975832935757617]
null_resource.storage_bucket: Destruction complete after 0s
null_resource.storage_bucket: Creating...
    }

Plan: 2 to add, 0 to change, 1 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

null_resource.storage_bucket: Destroying... [id=7756975832935757617]
null_resource.storage_bucket: Destruction complete after 0s
null_resource.storage_bucket: Creating...

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

null_resource.storage_bucket: Destroying... [id=7756975832935757617]
null_resource.storage_bucket: Destruction complete after 0s
null_resource.storage_bucket: Creating...
  Only 'yes' will be accepted to approve.

  Enter a value: yes

null_resource.storage_bucket: Destroying... [id=7756975832935757617]
null_resource.storage_bucket: Destruction complete after 0s
null_resource.storage_bucket: Creating...

null_resource.storage_bucket: Destroying... [id=7756975832935757617]
null_resource.storage_bucket: Destruction complete after 0s
null_resource.storage_bucket: Creating...
null_resource.storage_bucket: Destroying... [id=7756975832935757617]
null_resource.storage_bucket: Destruction complete after 0s
null_resource.storage_bucket: Creating...
null_resource.storage_bucket: Creating...
null_resource.storage_bucket: Provisioning with 'local-exec'...
null_resource.storage_bucket: Provisioning with 'local-exec'...
null_resource.storage_bucket (local-exec): Executing: ["python" "-c" "import pathlib; pathlib.Path(r'./buckets/hello-world-storage-bucket').mkdir(parents=True, exist_ok=True)"]
╷
│ Error: local-exec provisioner error
│
│   with null_resource.storage_bucket,
╷
│ Error: local-exec provisioner error
│
╷
│ Error: local-exec provisioner error
╷
╷
│ Error: local-exec provisioner error
│
│   with null_resource.storage_bucket,
│   with null_resource.storage_bucket,
│   on bucket.tf.json line 16, in resource.null_resource.storage_bucket.provisioner[0].local-exec:
│   16:             }
│
│ Error running command 'import pathlib; pathlib.Path(r'./buckets/hello-world-storage-bucket').mkdir(parents=True,
│ exist_ok=True)': exec: "python": executable file not found in $PATH. Output:
╵
bianca007@MSI:/mnt/c/Users/Bianca/Documents/Laboratorio7/Facade$ grep -R --line-number '"python"' labs/Laboratorio7/Facade || true
grep: labs/Laboratorio7/Facade: No such file or directory
bianca007@MSI:/mnt/c/Users/Bianca/Documents/Laboratorio7/Facade$ terraform apply -auto-approve
null_resource.storage_bucket: Refreshing state... [id=1646601161420265245]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  + create
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # null_resource.bucket_access will be created
  + resource "null_resource" "bucket_access" {
      + id       = (known after apply)
      + triggers = {
          + "bucket" = "hello-world-storage-bucket"
          + "entity" = "allAuthenticatedUsers"
          + "role"   = "READER"
        }
    }

  # null_resource.storage_bucket is tainted, so must be replaced
-/+ resource "null_resource" "storage_bucket" {
      ~ id       = "1646601161420265245" -> (known after apply)
        # (1 unchanged attribute hidden)
    }
    }

Plan: 2 to add, 0 to change, 1 to destroy.
null_resource.storage_bucket: Destroying... [id=1646601161420265245]
null_resource.storage_bucket: Destruction complete after 0s
null_resource.storage_bucket: Destruction complete after 0s
null_resource.storage_bucket: Creating...
null_resource.storage_bucket: Provisioning with 'local-exec'...
null_resource.storage_bucket: Creating...
null_resource.storage_bucket: Provisioning with 'local-exec'...
null_resource.storage_bucket: Provisioning with 'local-exec'...
null_resource.storage_bucket (local-exec): Executing: ["python3" "-c" "import pathlib; pathlib.Path(r'./buckets/hello-world-storage-bucket').mkdir(parents=True, exist_ok=True)"]
null_resource.storage_bucket: Creation complete after 0s [id=311004448280932377]
null_resource.bucket_access: Creating...
null_resource.storage_bucket (local-exec): Executing: ["python3" "-c" "import pathlib; pathlib.Path(r'./buckets/hello-world-storage-bucket').mkdir(parents=True, exist_ok=True)"]
null_resource.storage_bucket: Creation complete after 0s [id=311004448280932377]
null_resource.bucket_access: Creating...
null_resource.bucket_access: Provisioning with 'local-exec'...
null_resource.bucket_access (local-exec): Executing: ["python" "-c" "print('Acceso aplicado al bucket hello-world-storage-bucket')"]
╷
│ Error: local-exec provisioner error
null_resource.storage_bucket (local-exec): Executing: ["python3" "-c" "import pathlib; pathlib.Path(r'./buckets/hello-world-storage-bucket').mkdir(parents=True, exist_ok=True)"]
null_resource.storage_bucket: Creation complete after 0s [id=311004448280932377]
null_resource.bucket_access: Creating...
null_resource.bucket_access: Provisioning with 'local-exec'...
null_resource.bucket_access (local-exec): Executing: ["python" "-c" "print('Acceso aplicado al bucket hello-world-storage-bucket')"]
null_resource.storage_bucket (local-exec): Executing: ["python3" "-c" "import pathlib; pathlib.Path(r'./buckets/hello-world-storage-bucket').mkdir(parents=True, exist_ok=True)"]
null_resource.storage_bucket: Creation complete after 0s [id=311004448280932377]
null_resource.bucket_access: Creating...
null_resource.bucket_access: Provisioning with 'local-exec'...
null_resource.bucket_access (local-exec): Executing: ["python" "-c" "print('Acceso aplicado al bucket hello-world-storage-bucketnull_resource.storage_bucket (local-exec): Executing: ["python3" "-c" "import pathlib; pathlib.Path(r'./buckets/hello-world-storage-bucket').mkdir(parents=True, exist_ok=True)"]
null_resource.storage_bucket: Creation complete after 0s [id=311004448280932377]
null_resource.bucket_access: Creating...
age-bucket').mkdir(parents=True, exist_ok=True)"]
null_resource.storage_bucket: Creation complete after 0s [id=311004448280932377]
null_resource.bucket_access: Creating...
null_resource.storage_bucket: Creation complete after 0s [id=311004448280932377]
null_resource.bucket_access: Creating...
null_resource.bucket_access: Creating...
null_resource.bucket_access: Provisioning with 'local-exec'...
null_resource.bucket_access (local-exec): Executing: ["python" "-c" "print('Acceso aplicado al bucket hello-world-storage-bucketnull_resource.bucket_access: Provisioning with 'local-exec'...
null_resource.bucket_access (local-exec): Executing: ["python" "-c" "print('Acceso aplicado al bucket hello-world-storage-bucket')"]
╷
│ Error: local-exec provisioner error
╷
╷
╷
│ Error: local-exec provisioner error
│
│   with null_resource.bucket_access,
│   on bucket_access.tf.json line 21, in resource.null_resource.bucket_access.provisioner[0].local-exec:
│   21:             }
│
│ Error running command 'print('Acceso aplicado al bucket hello-world-storage-bucket')': exec: "python": executable file not    
│ found in $PATH. Output:
╵
╷
│ Error: local-exec provisioner error
│
│   with null_resource.bucket_access,
│   on bucket_access.tf.json line 21, in resource.null_resource.bucket_access.provisioner[0].local-exec:
│   21:             }
│
╷
│ Error: local-exec provisioner error
│
╷
╷
│ Error: local-exec provisioner error
│
│   with null_resource.bucket_access,
│   on bucket_access.tf.json line 21, in resource.null_resource.bucket_access.provisioner[0].local-exec:
│   21:             }
│
│ Error running command 'print('Acceso aplicado al bucket hello-world-storage-bucket')': exec: "python": executable file not    
│ found in $PATH. Output:
╵
```



### Facade

```
bianca007@MSI:/mnt/c/Users/Bianca/Documents/Laboratorio7/Facade$ cd ..
bianca007@MSI:/mnt/c/Users/Bianca/Documents/Laboratorio7$ ls
Adapter  Facade  Instrucciones.md  Inversion_control  Inyeccion_dependencias  Mediator
bianca007@MSI:/mnt/c/Users/Bianca/Documents/Laboratorio7$ cd Inversion_control
bianca007@MSI:/mnt/c/Users/Bianca/Documents/Laboratorio7/Inversion_control$ make prepare  
bianca007@MSI:/mnt/c/Users/Bianca/Documents/Laboratorio7/Inversion_control$ make network   
cd network && TF_DATA_DIR=/mnt/c/Users/Bianca/Documents/Laboratorio7/Inversion_control/.terraform TF_PLUGIN_CACHE_DIR=/mnt/c/Users/Bianca/Documents/Laboratorio7/Inversion_control/.terraform/plugin-cache TMP=/mnt/c/Users/Bianca/Documents/Laboratorio7/Inversion_control/.terraform/tmp TEMP=/mnt/c/Users/Bianca/Documents/Laboratorio7/Inversion_control/.terraform/tmp terraform init -upgrade -no-color && \
TF_DATA_DIR=/mnt/c/Users/Bianca/Documents/Laboratorio7/Inversion_control/.terraform TF_PLUGIN_CACHE_DIR=/mnt/c/Users/Bianca/Documents/Laboratorio7/Inversion_control/.terraform/plugin-cache TMP=/mnt/c/Users/Bianca/Documents/Laboratorio7/Inversion_control/.terraform/tmp TEMP=/mnt/c/Users/Bianca/Documents/Laboratorio7/Inversion_control/.terraform/tmp terraform apply -auto-approve -no-color
Initializing the backend...
Initializing provider plugins...
- Finding hashicorp/null versions matching "~> 3.2"...
- Finding hashicorp/local versions matching "~> 2.5"...
- Installing hashicorp/null v3.2.4...
- Installed hashicorp/null v3.2.4 (signed by HashiCorp)
- Installing hashicorp/local v2.5.3...
- Installed hashicorp/local v2.5.3 (signed by HashiCorp)
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  + create

Terraform will perform the following actions:

  # local_file.network_state will be created
  + resource "local_file" "network_state" {
      + content              = jsonencode(
            {
              + outputs = {
                  + cidr = {
                      + type  = "string"
                      + value = "10.0.0.0/16"
                    }
                  + name = {
                      + type  = "string"
                      + value = "hello-world-subnet"
                    }
                }
            }
        )
      + content_base64sha256 = (known after apply)
      + content_base64sha512 = (known after apply)
      + content_md5          = (known after apply)
      + content_sha1         = (known after apply)
      + content_sha256       = (known after apply)
      + content_sha512       = (known after apply)
      + directory_permission = "0777"
      + file_permission      = "0777"
      + filename             = "network_outputs.json"
      + id                   = (known after apply)
    }

  # null_resource.network will be created
  + resource "null_resource" "network" {
      + id       = (known after apply)
      + triggers = {
          + "render_time" = (known after apply)
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.
null_resource.network: Creating...
null_resource.network: Creation complete after 0s [id=4647999761777177100]
local_file.network_state: Creating...
local_file.network_state: Creation complete after 0s [id=d9e6632b7b6fe51a56c55fab21bc32b9df7fc2c0]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

bianca007@MSI:/mnt/c/Users/Bianca/Documents/Laboratorio7/Inversion_control$ make server 
cd network && TF_DATA_DIR=/mnt/c/Users/Bianca/Documents/Laboratorio7/Inversion_control/.terraform TF_PLUGIN_CACHE_DIR=/mnt/c/Users/Bianca/Documents/Laboratorio7/Inversion_control/.terraform/plugin-cache TMP=/mnt/c/Users/Bianca/Documents/Laboratorio7/Inversion_control/.terraform/tmp TEMP=/mnt/c/Users/Bianca/Documents/Laboratorio7/Inversion_control/.terraform/tmp terraform init -upgrade -no-color && \
TF_DATA_DIR=/mnt/c/Users/Bianca/Documents/Laboratorio7/Inversion_control/.terraform TF_PLUGIN_CACHE_DIR=/mnt/c/Users/Bianca/Documents/Laboratorio7/Inversion_control/.terraform/plugin-cache TMP=/mnt/c/Users/Bianca/Documents/Laboratorio7/Inversion_control/.terraform/tmp TEMP=/mnt/c/Users/Bianca/Documents/Laboratorio7/Inversion_control/.terraform/tmp terraform apply -auto-approve -no-color
Initializing the backend...
Initializing provider plugins...
- Finding hashicorp/null versions matching "~> 3.2"...
- Finding hashicorp/local versions matching "~> 2.5"...
- Using previously-installed hashicorp/null v3.2.4
- Using previously-installed hashicorp/local v2.5.3

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
null_resource.network: Refreshing state... [id=4647999761777177100]
local_file.network_state: Refreshing state... [id=d9e6632b7b6fe51a56c55fab21bc32b9df7fc2c0]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # null_resource.network must be replaced
-/+ resource "null_resource" "network" {
      ~ id       = "4647999761777177100" -> (known after apply)
      ~ triggers = { # forces replacement
          ~ "render_time" = "2025-11-11T14:36:45Z" -> (known after apply)
        }
    }

Plan: 1 to add, 0 to change, 1 to destroy.
null_resource.network: Destroying... [id=4647999761777177100]
null_resource.network: Destruction complete after 0s
null_resource.network: Creating...
null_resource.network: Creation complete after 0s [id=4438227689882830920]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.
```

### Inyeccion_dependencias

bianca007@MSI:/mnt/c/Users/Bianca/Documents/Laboratorio7/Inyeccion_dependencias/network$ terraform init && terraform apply -auto-approve
Initializing the backend...
Initializing provider plugins...
- Finding hashicorp/null versions matching "~> 3.2"...
- Finding hashicorp/local versions matching "~> 2.1"...
- Installing hashicorp/local v2.5.3...
- Installed hashicorp/local v2.5.3 (signed by HashiCorp)
- Installing hashicorp/null v3.2.4...
- Installed hashicorp/null v3.2.4 (signed by HashiCorp)
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  + create

Terraform will perform the following actions:

  # local_file.network_metadata will be created
  + resource "local_file" "network_metadata" {
      + content              = jsonencode(
            {
              + cidr = "10.0.0.0/28"
              + name = "hello-local-network"
            }
        )
      + content_base64sha256 = (known after apply)
      + content_base64sha512 = (known after apply)
      + content_md5          = (known after apply)
      + content_sha1         = (known after apply)
      + content_sha256       = (known after apply)
      + content_sha512       = (known after apply)
      + directory_permission = "0777"
      + file_permission      = "0777"
      + filename             = "./network_metadata.json"
      + id                   = (known after apply)
    }

  # null_resource.network will be created
  + resource "null_resource" "network" {
      + id       = (known after apply)
      + triggers = {
          + "cidr" = "10.0.0.0/28"
          + "name" = "hello-local-network"
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.
null_resource.network: Creating...
null_resource.network: Creation complete after 0s [id=7887757544095374689]
local_file.network_metadata: Creating...
local_file.network_metadata: Creation complete after 0s [id=e9543ac15ec3287348a6e4ea61cc91a715b3e29b]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

bianca007@MSI:/mnt/c/Users/Bianca/Documents/Laboratorio7/Inyeccion_dependencias$ terraform init && terraform apply -auto-approve
Initializing the backend...
Initializing provider plugins...
- Finding latest version of hashicorp/null...
- Installing hashicorp/null v3.2.4...
- Installed hashicorp/null v3.2.4 (signed by HashiCorp)
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  + create

Terraform will perform the following actions:
```


### Mediator

```
bianca007@MSI:/mnt/c/Users/Bianca/Documents/Laboratorio7/Mediator$ terraform init && terraform apply -auto-approve
Initializing the backend...
Initializing provider plugins...
- Finding latest version of hashicorp/null...
- Installing hashicorp/null v3.2.4...
- Installed hashicorp/null v3.2.4 (signed by HashiCorp)
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!



-...
ull_resource.server: Creating...
null_resource.firewall: Creating...
null_resource.network: Creation complete after 0s [id=6355123172332145834]
null_resource.firewall: Creation complete after 0s [id=3849064918008947978]
          + "name"       = "hello-world-server"
        }
    }

Plan: 3 to add, 0 to change, 0 to destroy.
null_resource.network: Creating...
null_resource.server: Creating...
null_resource.firewall: Creating...
null_resource.network: Creation complete after 0s [id=6355123172332145834]
null_resource.firewall: Creation complete after 0s [id=3849064918008947978]
null_resource.server: Creation complete after 0s [id=5271071209854630996]

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.


```


