<div className="row">
  <div className="col-12">
    <div className="card">
      <div className="card-header text-dark">Credit Card Transaction History</div>
      <div className="card-body">
        <div className="row">
          <div className="col-auto">
            <IconButton onClick={handleOpenDatePicker}>
              <DownloadIcon />
            </IconButton>
          </div>
          <div className={`col-auto ${!openDatePicker ? 'd-none' : ''}`}>
            <!-- Date picker component here -->
          </div>
          <div className={`col ${openDatePicker ? 'offset-md-3' : ''}`}>
            <!-- Transaction history table or content here -->
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
