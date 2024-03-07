// ... other imports ...
import { Modal, Button } from 'react-bootstrap'; // Make sure to import Modal and Button from 'react-bootstrap'

const Loading = ({ text, isSuccess, showModal, handleClose }) => {
  return (
    <Modal show={showModal} onHide={handleClose} centered>
      <Modal.Body>
        {isSuccess ? (
          <div className="text-success d-flex justify-content-center align-items-center">
            <i className="bi bi-check-circle-fill"></i>
            <span className="ml-2">{text}</span>
          </div>
        ) : (
          <div className="d-flex justify-content-center">
            <div className="spinner-border text-primary" role="status">
              <span className="sr-only">Loading...</span>
            </div>
          </div>
        )}
      </Modal.Body>
      <Modal.Footer>
        <Button variant="primary" onClick={handleClose}>
          OK
        </Button>
      </Modal.Footer>
    </Modal>
  );
};

export default Loading;














import React, { useState } from 'react';
import Loading from './Loading'; // Adjust the import path as needed

const TransactionsComponent = () => {
  // ... other state hooks ...

  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    // ... fetch transactions as before ...
  }, []);

  const handleProcessingAllTransaction = async () => {
    if (isProcessing) return;

    setIsProcessing(true);
    setShowModal(true); // Show modal while processing

    try {
      const processTransactions = await processAllTransactions();
      setTransactions(processTransactions);
      // Update text to show success message
      setModalText('All transactions have been processed successfully!');
      setIsSuccess(true); // Set success to true
    } catch (error) {
      // Handle error
      setModalText('Failed to process transactions.');
      setIsSuccess(false); // Set success to false
    } finally {
      setIsProcessing(false);
      // Do not close the modal automatically. User must click OK.
    }
  };

  // Function to handle closing of the modal
  const handleCloseModal = () => {
    setShowModal(false);
  };

  // ... other render code ...

  return (
    <div>
      {/* ... */}

      {/* Trigger the processing of all transactions */}
      <button onClick={handleProcessingAllTransaction}>
        Process Transactions
      </button>

      {/* Loading modal component */}
      <Loading
        text={modalText} // This state should hold the message to display
        isSuccess={isSuccess} // This state should represent the success status
        showModal={showModal} // This state controls the visibility of the modal
        handleClose={handleCloseModal} // Function to close the modal
      />

      {/* ... */}
    </div>
  );
};

export default TransactionsComponent;
