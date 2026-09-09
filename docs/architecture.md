# ResumeForge Architecture

1. High-Level Overview

2. Project Layers

3. Dependency Graph

4. Generation Pipeline

5. Profile Management

6. Future Extensions

# High-Level Diagram

CLI
|
Responsible only for parsing arguments.
No business logic.
↓
CLIWorkflow
|
Coordinates commands.
Handles command dispatch.
No resume generation logic.
↓
Bootstrap
|
Creates dependencies.
Acts as the composition root.
↓
ResumeGenerator
|

↓
Pipeline
|

↓
Output

## Goals

- Single source of truth for resume data
- Multiple output formats
- Multiple resume profiles
- Clean modular architecture
- Automated testing

## Project Structure

...