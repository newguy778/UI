fetch(url)
  .then(response => {
    const contentLength = response.headers.get('content-length');
    if (contentLength <= 0) {
      alert('File is empty or content-length is 0');
      return Promise.reject('File is empty'); // Reject the promise to stop further execution
    }
    return response.blob();
  })
  .then(blob => {
    // Rest of the code...
  })
  .catch(error => {
    if (error !== 'File is empty') {
      console.error('Unable to download file', error);
    }
  });
