markdown
# Interactive Dashboard for Analyzing SAIFI Data

## Overview
This project provides an interactive dashboard for analyzing the Annual SAIFI (System Average Interruption Frequency Index) data from 2013 to 2025. The dashboard allows users to visualize trends, conduct comparative analyses, and generate predictive insights to better understand energy reliability in Abu Dhabi and beyond.

## Features
1. **Dynamic Charts and Graphs**: Explore data trends over time.
2. **Benchmarking Tools**: Compare regional SAIFI performance.
3. **Predictive Analytics**: Forecast future power interruptions.
4. **Customizable Reports**: Generate tailored reports.
5. **User-Friendly Interface**: Accessible to users with varying technical expertise.

## Requirements
- Python 3.7+
- pandas
- matplotlib
- seaborn

## Getting Started
1. Clone this repository to your local machine:
   bash
   git clone https://github.com/your-repo/saifi-dashboard.git
   
2. Navigate to the project directory:
   bash
   cd saifi-dashboard
   
3. Install the required Python libraries:
   bash
   pip install pandas matplotlib seaborn
   
4. Place the `SAIFI.csv` dataset in the project directory.

## Running the Example Code
1. Open the `saifi_analysis.py` script in your Python editor.
2. Run the script to generate a line plot showing the SAIFI trend over time:
   bash
   python saifi_analysis.py
   
3. The output will include:
   - A line plot (`saifi_trend.png`) visualizing the SAIFI trend.
   - Summary statistics (mean, max, min SAIFI values) printed to the console.
   - A CSV file (`saifi_summary.csv`) containing the summary statistics.

## Future Enhancements
- Add interactive visualization using Plotly or Dash.
- Implement predictive analytics using machine learning models.
- Include data filtering and advanced analytics options.

## Contributing
We welcome contributions! Please fork the repository and open a pull request with your changes.

## License
This project is licensed under the Open Data License.

## Contact
For questions or feedback, please contact [energydata@abudhabi.ae](mailto:energydata@abudhabi.ae).
