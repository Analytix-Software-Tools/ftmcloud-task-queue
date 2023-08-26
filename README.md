# ftmcloud Task Queue Worker

## Overview
The ```ftmcloud``` Task Queue Worker application is a Celery-based application designed to trigger bulk processing and
ingestion tasks.

## Structure

### core
Contains logic relating to the core application functionality as well as logic that is crosscutting.

### tasks
Contains domain-specific task logic that can be executed at any point in time.