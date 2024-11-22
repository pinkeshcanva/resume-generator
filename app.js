document.getElementById('generator-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const jobTitle = document.getElementById('job_title').value;
    const experience = document.getElementById('experience').value;
    const companyInfo = document.getElementById('company_info').value;
    const templateType = document.getElementById('template_type').value;

    // Show loading message
    document.getElementById('loading').style.display = 'block';

    try {
        const response = await fetch('http://localhost:5000/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ job_title: jobTitle, experience: experience, company_info: companyInfo, template_type: templateType }),
        });

        const result = await response.json();
        document.getElementById('loading').style.display = 'none';

        if (response.ok) {
            const generatedText = result.generated_text;
            document.getElementById('output').innerText = generatedText;

            // Show the download PDF button
            document.getElementById('download-pdf').style.display = 'block';

            // Add event listener to the PDF download button
            document.getElementById('download-pdf').addEventListener('click', () => {
                const element = document.getElementById('output'); // Get the content to download
                html2pdf(element); // Trigger PDF download
            });
        } else {
            document.getElementById('output').innerText = "Error generating content. Please try again.";
        }
    } catch (error) {
        document.getElementById('loading').style.display = 'none';
        document.getElementById('output').innerText = `An error occurred: ${error.message}`;
    }
});
