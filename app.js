document.getElementById('generator-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const jobTitle = document.getElementById('job_title').value;
    const experience = document.getElementById('experience').value;
    const companyInfo = document.getElementById('company_info').value;
    const templateType = document.getElementById('template_type').value;

    const response = await fetch('http://localhost:5000/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ job_title: jobTitle, experience: experience, company_info: companyInfo, template_type: templateType }),
    });

    const result = await response.json();
    document.getElementById('output').innerText = result.generated_text;
});
