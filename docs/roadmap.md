# Roadmap

## Step 1: Complete the Control Library

Migrate all 46 Control Baseline requirements into structured YAML. The current repository contains representative Level 1, Level 2, and Level 3 examples.

## Step 2: Complete Platform Capability Mapping

Extend `platform/platform-capabilities.yaml` until every relevant control requirement has at least one mapped platform capability.

## Step 3: Generate Traceability Outputs

Create scripts to generate:

- Control-to-platform traceability matrix
- Control-to-evidence matrix
- Policy candidate matrix
- Open gap report

## Step 4: Select Pilot Repository

Select a demo or real project repository and define the input model for:

- repository configuration
- pipeline evidence
- artifact metadata
- SBOM metadata
- vulnerability findings
- waivers

## Step 5: Run Initial Policy-as-Code Gates

Start with:

1. branch protection
2. SBOM required
3. vulnerability scan required
4. critical vulnerability waiver handling
5. artifact digest or signature required
6. dependency source control
7. Infrastructure as Code presence
8. waiver validity

## Step 6: Decide Source-of-Truth Model

After the pilot, decide whether YAML becomes the formal master source or remains synchronized with an external BMS/document management system.
