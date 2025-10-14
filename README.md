# D-Node

> An environment lockdown concept powered by Python scripts to harden servers before deployment. It systematically removes non-essential components to minimize the attack surface. Automate your secure baseline configuration and ensure every node is a "D-Node"—simple, focused, and secure.

-----

## About D-Node

D-Node is a utility and a philosophy for proactive server security. In a typical server setup, the default configuration includes numerous services, open ports, and software packages that are unnecessary for the server's specific role. Each of these components expands the system's **attack surface**, creating potential vulnerabilities for attackers to exploit.

The D-Node concept is simple: a server should be a focused, single-purpose system. It should only have the exact tools and configurations needed to perform its one job, and nothing more. This project provides the tools to automate this lockdown process, ensuring any new node is hardened before it is deployed into a production environment.

-----

## Core Concepts: Secure-by-Design and IaC

D-Node is a practical implementation of several key cybersecurity principles that are considered best practices in the industry.

  * **Server Hardening**: This is the process of minimizing a server's vulnerabilities. D-Node accomplishes this by systematically removing unused software, disabling services, closing unnecessary ports, and enforcing secure configurations.
  * **Secure-by-Design**: This approach integrates security into every phase of the system lifecycle. Instead of trying to add security measures after a system is built, D-Node ensures the server is secure from the moment it is provisioned.
  * **Infrastructure as Code (IaC)**: By using scripts and playbooks to define and apply security configurations, D-Node embodies the IaC principle. This makes the hardening process **repeatable**, **consistent**, and **auditable**, eliminating the risk of human error.

-----

## The D-Node Automation Stack

D-Node provides a holistic approach to automation, starting with a secure foundation and extending to the entire operational stack. The project is built on the belief that a hardened node is just the first step; true automation requires tools for provisioning, workflow, and specialized applications.

  * **The Foundation (Configuration & Hardening)**: The core of D-Node is creating a secure baseline. We champion **Ansible** for its agentless power and **Python** for its utility and safety. This combination ensures every server starts as a secure and consistent "D-Node."
  * **The Environment (Provisioning)**: Before a node can be hardened, it must exist. D-Node includes tools like **Vagrant** to automate the creation of reproducible development and testing environments, ensuring consistency from the very beginning.
  * **The Engine (Workflow & AI Automation)**: Once a node is secure, it needs to perform tasks. D-Node provides standardized setups for powerful engines like **Apache Airflow** for code-based data pipelines and **n8n** for low-code AI and API-driven workflows.
  * **The Application (MLOps)**: For specialized tasks, D-Node supports the MLOps lifecycle. By providing a setup for **MLflow**, we enable teams to manage machine learning models on an infrastructure that is secure and automated from the ground up.

-----

## Automation Tool Matrix

| Category | Primary Goal | Analogy 💡 | Key Function | Primary Tool | Alternative Tools |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Configuration Mgmt** | Maintain systems in a consistent, desired state. | A **Blueprint Enforcer** 📜 | Installs/configures software, manages files, and prevents "configuration drift." | **Ansible** | SaltStack, CFEngine, Puppet, Chef |
| **Orchestration** | Coordinate multiple systems to work as a cohesive application. | An **Orchestra Conductor** 🎶 | Manages the lifecycle of complex, multi-container applications and services. | **Ansible** | Docker Swarm, Kubernetes, Apache Mesos |
| **Workflow Automation** | Manage and schedule sequences of dependent tasks. | A **Project Manager** 🗓️ | Executes code-driven data pipelines (ETL/ELT) and manages batch job dependencies. | **Apache Airflow** | Luigi, Prefect |
| **Provisioning** | Create and manage the underlying infrastructure itself. | A **Construction Crew** 🏗️ | Builds servers, VMs, networks, and other cloud resources from code. | **Vagrant** | Terraform, AWS CloudFormation |
| **AI Automation** | Integrate AI services and apps to automate complex tasks. | A **Digital Nervous System** 🧠 | Builds and executes workflows by connecting APIs and AI models, often low-code. | **n8n** | - |
| **MLOps** | Automate the machine learning lifecycle. | An **AI Assembly Line** 🤖 | Manages the process of training, deploying, and monitoring ML models. | **MLflow** | Kubeflow, Seldon Core |

-----

## Getting Started

These instructions will get you a copy of the project up and running to harden your first node.

### Prerequisites

  * Python 3.8+ and `pip`
  * Ansible 2.9+
  * `git` to clone the repository

### Installation & Usage

1.  **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/d-node.git
    cd d-node
    ```
2.  **Install requirements**:
    ```sh
    pip install -r requirements.txt
    ```
3.  **Set up your Ansible inventory** file (`hosts`) with the target server's IP address.
4.  **Run a Pre-Flight Check (Python)**: Use a utility script to check connectivity before making changes.
    ```sh
    python tools/check_node.py --target 192.168.1.100
    ```
5.  **Apply the Hardening Playbook (Ansible)**: Execute the main Ansible playbook to configure the server.
    ```sh
    ansible-playbook -i hosts harden_server.yml --limit 192.168.1.100
    ```

-----

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

-----

## License

This project is an open-source software released under the **MIT License**. See the `LICENSE` file for more details.
