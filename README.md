import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'; // Make sure you have Bootstrap CSS imported

const Loading = ({ text, isSuccess }) => {
  return (
    <div className="modal show" tabIndex="-1" role="dialog" style={{ display: 'block' }}>
      <div className="modal-dialog" role="document">
        <div className="modal-content">
          <div className="modal-header">
            <h5 className="modal-title">Status</h5>
            <button type="button" className="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div className="modal-body d-flex justify-content-center">
            {isSuccess ? (
              <>
                <div className="alert alert-success" role="alert">
                  <i className="bi bi-check-circle-fill"></i> {text}
                </div>
              </>
            ) : (
              <div className="spinner-border spinner-border-lg" role="status">
                <span className="sr-only">Loading...</span>
              </div>
            )}
          </div>
          <div className="modal-footer">
            <button type="button" className="btn btn-primary" data-dismiss="modal">OK</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Loading;
