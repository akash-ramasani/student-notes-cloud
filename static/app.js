document.addEventListener('DOMContentLoaded', () => {
    console.log('Student Notes Cloud Initialized');
    createToastContainer();
});

function createToastContainer() {
    if (!document.getElementById('toast-container')) {
        const container = document.createElement('div');
        container.id = 'toast-container';
        document.body.appendChild(container);
    }
}

function showToast(message, type = 'success') {
    const container = document.getElementById('toast-container');
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.innerHTML = `
        <span class="toast-message">${message}</span>
    `;
    
    container.appendChild(toast);
    
    // Auto remove
    setTimeout(() => {
        toast.style.animation = 'fadeOut 0.3s ease forwards';
        setTimeout(() => toast.remove(), 300);
    }, 4000);
}

async function handleFileUpload(event) {
    const file = event.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('note', file);

    const uploadBtn = event.target.nextElementSibling;
    const originalText = uploadBtn.innerText;
    uploadBtn.innerText = 'Uploading...';
    uploadBtn.disabled = true;

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            showToast('Note uploaded successfully!');
            setTimeout(() => window.location.reload(), 1000);
        } else {
            const data = await response.json();
            showToast(data.error || 'Upload failed', 'error');
        }
    } catch (err) {
        console.error('Error:', err);
        showToast('An error occurred during upload.', 'error');
    } finally {
        uploadBtn.innerText = originalText;
        uploadBtn.disabled = false;
    }
}

// Helper to confirm actions
function confirmAction(message) {
    return confirm(message);
}
