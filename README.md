# Virgin Media Competitor Analysis API

## Overview

This API is designed to help companies (such as Infosys) identify competitors that have worked with a given target account (e.g., **Virgin Media**). The API fetches details of companies that have partnered with Virgin Media, including the nature of their collaboration and a link to the source of the information.

By using this API, companies can save time and resources that would otherwise be spent on manual research and analysis of competitors. This tool can automatically gather and display competitor information, streamlining the process of identifying potential leads.

## Features

- **Fetch Competitor Information**: Retrieve a list of competitors that have worked with Virgin Media, including a brief description of the collaboration.
- **Proof of Collaboration**: Provides a direct link to the source or a brief description of the work done by each competitor.
- **JSON Response**: Returns data in a structured format that can easily be consumed by other applications or services.

## Tech Stack

- **Backend**: Python, FastAPI
- **Data**: Hardcoded data (research data on collaborations between Virgin Media and competitors)
- **Database**: None (Static data)
- **Hosting**: Local development environment (can be deployed to a platform like Heroku or AWS)

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Steps to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/sahil-vanarse/virgin-media.git

2. Go to Virgin-Media:
   ```bash
   cd virgin-media

3. Install Requirements:
   ```bash
   pip install -r requirements.txt


4. Run the Local Host:
   ```bash
   uvicorn main:app --reload

   
