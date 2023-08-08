

import { useState } from 'react';

export const useDownloadWithModal = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [status, setStatus] = useState<'downloading' | 'downloaded' | 'error'>('downloading');
  const [message, setMessage] = useState('Downloading...');

  const openDownloadModal = async (downloadUrl: string, parameterName: string) => {
    setIsOpen(true);
    setStatus('downloading');
    setMessage('Downloading...');

    try {
      const response = await fetch(downloadUrl);
      if (!response.ok) {
        throw new Error('Download failed');
      }

      const blob = await response.blob();
      const filename = `downloaded-${parameterName}.xlsx`; // Adjust the filename as needed

      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = filename;
      a.click();
      window.URL.revokeObjectURL(url);

      setStatus('downloaded');
      setMessage('Downloaded successfully!');
    } catch (error) {
      setStatus('error');
      setMessage('An error occurred while downloading the file.');
    }
  };

  const closeModal = () => {
    setIsOpen(false);
  };

  return { isOpen, status, message, openDownloadModal, closeModal };
};
