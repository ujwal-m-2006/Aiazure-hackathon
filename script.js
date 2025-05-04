// Trigger file input when clicking the drop area
document.getElementById('drop-area').addEventListener('click', function () {
  document.getElementById('resume-upload').click();
});

// Handle file selection
document.getElementById('resume-upload').addEventListener('change', function (e) {
  const file = e.target.files[0];
  if (file) {
      alert(`File "${file.name}" selected.`);
  }
});

// Handle Analyze button click
document.getElementById('analyze-btn').addEventListener('click', function () {
  const jobTitle = document.getElementById('job-title').value;
  const location = document.getElementById('job-location').value;
  const experience = document.getElementById('experience-level').value;

  if (!jobTitle || !location || !experience) {
      alert("Please fill out all fields before analyzing.");
      return;
  }

  // Show results section (simulate analysis)
  document.getElementById('results-section').scrollIntoView({ behavior: 'smooth' });

  // In real use: send data to the backend with fetch() or AJAX
});

// Tab switching functionality
const tabs = document.querySelectorAll('.tab');
const contents = document.querySelectorAll('.tab-content');

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
      // Remove active from all tabs and hide all content
      tabs.forEach(t => t.classList.remove('active'));
      contents.forEach(c => c.style.display = 'none');

      // Activate clicked tab and show its content
      tab.classList.add('active');
      document.getElementById(tab.dataset.tab).style.display = 'block';
  });
});
