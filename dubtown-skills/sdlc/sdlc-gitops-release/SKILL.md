---
name: sdlc-gitops-release
description: "Use during ship when Git is the single declarative source of truth for both application and infrastructure/cluster state, with an in-cluster agent continuously reconciling actual state toward it. Activates when someone says \"how do we deploy to Kubernetes\", \"how do we manage cluster state or config drift\", \"make releases declarative and auditable\", or when desired-vs-actual state is a first-class concern. Inverts push-based CI/CD into pull-based reconciliation — any manual drift is detected and corrected."
stage: ship
posture: gitops-release
tier: 2
role: skill
license: MIT
---
# Skill: GitOps Release

## Lineage

GitOps was coined by Alexis Richardson (Weaveworks CEO) in 2017 and formalized through the OpenGitOps specification (CNCF). It extends Continuous Delivery to infrastructure by treating Git as the single source of truth for both application code and cluster state. The approach was catalyzed by the rise of Kubernetes and declarative infrastructure tooling, where the gap between "desired state" and "actual state" became a first-class operational concern.

---

## Core Principle

> "The entire system is described declaratively. Git is the source of truth. Approved changes are automatically applied. Software agents ensure correctness and alert on divergence."
>
> - OpenGitOps Principles

GitOps inverts the push model of traditional CI/CD. Instead of a pipeline pushing artifacts to a cluster, a reconciliation agent running *inside* the cluster pulls desired state from Git and applies it continuously. The cluster is always converging toward what Git declares it should be. Any manual change to the cluster is immediately visible as "drift" and corrected.

The result: Git history is your complete audit trail. Rollback is a git revert. The cluster configuration is always reviewable, diff-able, and approvable.

---

## Key Concepts

| Concept | Description |
| --- | --- |
| **Desired State** | The declarative description of your system stored in Git: Kubernetes manifests, Helm charts, Kustomize overlays |
| **Actual State** | What is currently running in the live cluster |
| **Reconciliation** | The continuous process of comparing desired vs. actual state and applying changes to close the gap |
| **Drift** | Any difference between desired and actual state - treated as a defect to be corrected |
| **Reconciliation Agent** | The operator running in the cluster (Flux, ArgoCD) that performs reconciliation |

---

## Execution Steps

### 1. Repository Structure

Separate your application code repository from your configuration/infrastructure repository. The config repo is the declarative description of your production cluster.

```
config-repo/
  clusters/
    production/
      apps/
        my-service/
          deployment.yaml
          service.yaml
          kustomization.yaml
    staging/
      apps/
        ...
  infrastructure/
    ingress/
    monitoring/
    cert-manager/
```

### 2. Install the Reconciliation Agent

Bootstrap Flux or ArgoCD in your target cluster, pointing it at the config repo:

```bash
flux bootstrap github \
  --owner=my-org \
  --repository=config-repo \
  --branch=main \
  --path=clusters/production
```

The agent begins watching the repository. Any commit to main that changes the desired state triggers reconciliation.

### 3. The Release Workflow

When a new application version is ready to ship:

1. CI builds and pushes the Docker image to a registry with a new immutable tag (commit SHA digest preferred over mutable version tags).
2. A PR is opened against the config repo updating the image reference in the deployment manifest.
3. The PR is reviewed (code review applies to infrastructure changes too) and merged to main.
4. The reconciliation agent detects the change within minutes and applies it to the cluster.
5. No human runs `kubectl apply`. No pipeline has cluster credentials. The cluster pulls; it is not pushed to.

### 4. Drift Detection and Remediation

If someone manually modifies the cluster (`kubectl patch`, console change), the reconciliation agent detects drift and:

- **Auto-corrects** (recommended for production): reverts the manual change back to the Git-declared state.
- **Alerts** (for environments where manual intervention is sometimes expected): notifies the team of the divergence.

Manual changes to production that bypass Git are not just policy violations - they are operationally invisible and untraceable.

### 5. Rollback

Rollback is a Git operation, not a cluster operation:

```bash
git revert <commit-sha>
# or for a release tag rollback:
# update the image tag in the manifest to the previous version, open PR, merge
```

The reconciliation agent applies the reverted state automatically. The rollback is auditable, reviewable, and consistent across all environments that watch the repo.

---

## Secret Management

Secrets cannot live in Git in plaintext. Use one of these patterns:

| Approach | Tool | Notes |
| --- | --- | --- |
| Encrypted secrets in Git | Sealed Secrets, SOPS | Secrets are encrypted before commit; decrypted by a controller in-cluster |
| External secrets store | External Secrets Operator | Pulls secrets from Vault, AWS Secrets Manager, GCP Secret Manager at runtime |
| Image pull secrets via IRSA/Workload Identity | Cloud-native | No secret stored anywhere; cluster identity grants registry access |

---

## Failure Modes and Mitigations

| Failure Mode | Mitigation |
| --- | --- |
| Config repo diverges from what was tested in CI | Pin image references to SHA digest, not mutable tags like `latest` or `v1.2.3` |
| Reconciliation lag makes rollout feel slow | Tune reconciliation interval; add webhook push notifications from GitHub to the agent |
| Multi-cluster complexity creates config proliferation | Use hub-spoke topology with Kustomize overlays per environment; DRY config aggressively |
| Team treats the cluster as authoritative and bypasses Git | Enforce read-only cluster credentials for all humans; write access only via the reconciliation agent |

---

## Tooling Reference

| Tool | Notes |
| --- | --- |
| **Flux** | CNCF-graduated; pull-based; strong Helm and Kustomize support; lower UI surface area |
| **ArgoCD** | CNCF-graduated; UI-first; excellent multi-app visibility; widely adopted |
| **Crossplane** | Extends GitOps to cloud infrastructure provisioning beyond Kubernetes |
