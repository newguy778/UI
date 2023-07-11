

import React from 'react';

const MyComponent: React.FC = () => {
  return (
    <div className="flex items-center justify-between p-6 bg-white shadow-lg rounded-lg">
      <h1 className="text-4xl font-semibold text-gray-900">Title</h1>
      <div className="flex space-x-4">
        <button className="w-28 h-12 text-white bg-blue-500 rounded-lg shadow-md transition-transform duration-500 ease-in-out transform hover:-translate-y-1 hover:scale-110">View</button>
        <button className="w-28 h-12 text-white bg-green-500 rounded-lg shadow-md transition-transform duration-500 ease-in-out transform hover:-translate-y-1 hover:scale-110">Upload</button>
        <button className="w-28 h-12 text-white bg-purple-500 rounded-lg shadow-md transition-transform duration-500 ease-in-out transform hover:-translate-y-1 hover:scale-110">Download</button>
      </div>
    </div>
  );
}

export default MyComponent;
