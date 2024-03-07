<div className="card">
  <div className="card-header text-dark">Credit Card Transaction History</div>
  <div className="card-body">
    <div className="d-flex justify-content-between mb-3">
      <div>
        <input type="text" className="form-control mr-2" placeholder="Start Date" />
        <input type="text" className="form-control" placeholder="End Date" />
      </div>
      <button className="btn btn-primary">Process Transaction</button>
    </div>
    
    <!-- Other content -->
    
    <div className="table-responsive" style={{ maxHeight: '400px' }}>
      <table className="table table-striped">
        {/* Table header and rows */}
      </table>
    </div>
  </div>
</div>






<div className="card">
  <div className="card-header text-dark">Credit Card Transaction History</div>
  <div className="card-body">
    <div className="d-flex justify-content-between mb-3">
      <div>
        <input type="text" className="form-control mr-2" placeholder="Start Date" />
        <input type="text" className="form-control" placeholder="End Date" />
      </div>
      <button className="btn btn-primary">Process Transaction</button>
    </div>
    
    <!-- Other content -->
    
    <div className="table-responsive custom-scrollbar" style={{ maxHeight: '400px' }}>
      <table className="table table-striped">
        {/* Table header and rows */}
      </table>
    </div>
  </div>
</div>




.custom-scrollbar::-webkit-scrollbar {
  width: 8px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background-color: #f5f5f5;
  border-radius: 10px;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background-color: #888;
  border-radius: 10px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background-color: #555;
}
