
<div align="center">

<h1>🌲 Hyperparameter Optimization Using Tree of Thoughts (ToT)</h1>

<h3>
Intelligent Random Forest Hyperparameter Optimization using Large Language Models
</h3>

<p>
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn"/>
  <img src="https://img.shields.io/badge/LangChain-Framework-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Gemini-LLM-purple?style=for-the-badge&logo=google"/>
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge"/>
</p>

</div>

<hr>

<h2>📌 Project Overview</h2>

<p>
<b>Hyperparameter Optimization Using Tree of Thoughts (ToT)</b> is an intelligent Machine Learning project that combines
<b>Random Forest Hyperparameter Tuning</b> with <b>LLM-powered reasoning</b> to analyze tuning results and recommend optimal configurations.
</p>

<p>
Instead of simply selecting the best hyperparameters from <code>GridSearchCV</code>, this project leverages the
<b>Tree-of-Thoughts (ToT)</b> reasoning framework using <b>Google Gemini + LangChain</b> to provide deeper insights into:
</p>

<ul>
  <li>✅ Promising Hyperparameter Ranges</li>
  <li>✅ Bias vs Variance Analysis</li>
  <li>✅ Training Time vs Performance Tradeoff</li>
  <li>✅ Best Model Configuration</li>
  <li>✅ Final Recommendation with Justification</li>
</ul>

<p>
The system performs structured reasoning over tuning results and explains
<b>why a configuration works</b>, not just
<b>which configuration performs best</b>.
</p>

<hr>

<h2>🚀 Features</h2>

<h3>✨ Smart Hyperparameter Analysis</h3>

<ul>
  <li>Performs exhaustive <b>GridSearchCV</b> tuning for <b>Random Forest</b></li>
  <li>Tests multiple combinations of:
    <ul>
      <li><code>n_estimators</code></li>
      <li><code>max_depth</code></li>
      <li><code>min_samples_split</code></li>
      <li><code>min_samples_leaf</code></li>
      <li><code>max_features</code></li>
    </ul>
  </li>
</ul>

<h3>🧠 Tree-of-Thought Reasoning</h3>

<ul>
  <li>Uses <b>Gemini 2.5 Flash Lite</b></li>
  <li>Analyzes model tuning outputs using structured reasoning</li>
  <li>Produces explainable recommendations</li>
</ul>

<h3>📊 Performance Evaluation</h3>

<ul>
  <li>Cross-validation accuracy</li>
  <li>Train accuracy</li>
  <li>Overfitting gap analysis</li>
  <li>Training time comparison</li>
</ul>

<h3>🤖 LLM-Based Decision Making</h3>

<p>The model evaluates:</p>

<ol>
  <li><b>Promising Hyperparameter Ranges</b></li>
  <li><b>Bias-Variance Tradeoff</b></li>
  <li><b>Training Time vs Accuracy</b></li>
  <li><b>Best Configuration</b></li>
  <li><b>Final Justification</b></li>
</ol>

<hr>

<h2>🏗️ Project Architecture</h2>

<pre>
Dataset
   │
   ▼
Data Preprocessing
   │
   ▼
Random Forest Model
   │
   ▼
GridSearchCV Hyperparameter Tuning
   │
   ▼
Performance Metrics Extraction
   │
   ▼
Results Converted to Text
   │
   ▼
Prompt Engineering
   │
   ▼
Gemini LLM (Tree of Thoughts)
   │
   ▼
Hyperparameter Analysis & Recommendation
</pre>

<hr>

<h2>📂 Project Structure</h2>

<pre>
Hyperparameter-Optimization-Using-Tree-of-Thoughts/
│── main.py                 # Main execution file
│── model.py                # Gemini model configuration
│── prompt.py               # Tree-of-Thought prompt
│── ML.py                   # ML pipeline + GridSearchCV
│── requirements.txt        # Dependencies
│── .env                    # API keys
│── merged_crop_dataset.csv # Dataset
</pre>

<hr>

<h2>⚙️ Installation</h2>

<h3>1️⃣ Clone Repository</h3>

<pre>
git clone https://github.com/Manikantapulugala/Hyperparameter-Optimization-Using-Tree-of-Thoughts.git
</pre>

<h3>2️⃣ Move to Project Directory</h3>

<pre>
cd Hyperparameter-Optimization-Using-Tree-of-Thoughts
</pre>

<h3>3️⃣ Create Virtual Environment</h3>

<h4>Conda</h4>

<pre>
conda create -n tot python=3.10
conda activate tot
</pre>

<h4>Virtualenv</h4>

<pre>
python -m venv venv
venv\Scripts\activate
</pre>

<hr>

<h2>📦 Install Requirements</h2>

<pre>
pip install -r requirements.txt
</pre>

<hr>

<h2>🔑 Environment Variables</h2>

<p>Create a <code>.env</code> file:</p>

<pre>
GEMINI_KEY=your_google_gemini_api_key
</pre>

<hr>

<h2>▶️ Run Project</h2>

<pre>
python main.py
</pre>

<p>The system will:</p>

<ol>
  <li>Load Dataset</li>
  <li>Train Random Forest Model</li>
  <li>Perform Hyperparameter Tuning</li>
  <li>Generate Evaluation Results</li>
  <li>Send Results to Gemini</li>
  <li>Return Tree-of-Thought Analysis</li>
</ol>

<hr>

<h2>🛠️ Tech Stack</h2>

<table>
  <tr>
    <th>Technology</th>
    <th>Purpose</th>
  </tr>
  <tr>
    <td>Python</td>
    <td>Programming Language</td>
  </tr>
  <tr>
    <td>Scikit-Learn</td>
    <td>Machine Learning</td>
  </tr>
  <tr>
    <td>GridSearchCV</td>
    <td>Hyperparameter Tuning</td>
  </tr>
  <tr>
    <td>LangChain</td>
    <td>LLM Orchestration</td>
  </tr>
  <tr>
    <td>Gemini 2.5 Flash Lite</td>
    <td>Reasoning Engine</td>
  </tr>
  <tr>
    <td>Pandas</td>
    <td>Data Processing</td>
  </tr>
  <tr>
    <td>NumPy</td>
    <td>Numerical Computation</td>
  </tr>
  <tr>
    <td>Seaborn</td>
    <td>Visualization</td>
  </tr>
  <tr>
    <td>Matplotlib</td>
    <td>Plotting</td>
  </tr>
</table>

<hr>

<h2>🧠 Why Tree of Thoughts?</h2>

<p><b>Traditional Hyperparameter Optimization:</b></p>

<pre>
Best Score → Select Parameters
</pre>

<p><b>Tree of Thoughts Approach:</b></p>

<pre>
Evaluate Multiple Paths
       ↓
Compare Configurations
       ↓
Analyze Bias/Variance
       ↓
Reason About Tradeoffs
       ↓
Explain Best Choice
</pre>

<p>
This makes the optimization process more
<b>explainable</b>,
<b>interpretable</b>, and
<b>human-like</b>.
</p>

<hr>

<h2>📈 Sample Output</h2>

<pre>
1. Promising Hyperparameter Ranges:
- n_estimators between 100–200 performed consistently well.
- max_depth=None showed stronger accuracy.

2. Bias-Variance Analysis:
- Low overfitting observed for max_depth=10.
- Deeper trees increased variance.

3. Training Time vs Performance:
- 200 estimators improved performance but increased training time.

4. Best Configuration:
- n_estimators=100
- max_depth=10
- min_samples_split=2

5. Final Justification:
This configuration provides the best balance between
generalization and computational efficiency.
</pre>

<hr>

<h2>📌 Future Improvements</h2>

<ul>
  <li>Add support for <b>XGBoost & LightGBM</b></li>
  <li>Implement <b>Bayesian Optimization</b></li>
  <li>Build <b>Streamlit Dashboard</b></li>
  <li>Add visualization of ToT reasoning paths</li>
  <li>Multi-model comparison</li>
</ul>

<hr>

<h2>🤝 Contributing</h2>

<p>Contributions are welcome!</p>

<ol>
  <li>Fork the repository</li>
  <li>Create a new branch</li>
  <li>Commit changes</li>
  <li>Open a Pull Request</li>
</ol>
