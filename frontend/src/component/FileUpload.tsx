/* Importing the React library, the useState, useEffect, and ChangeEvent hooks from the React library,
the AxiosResponse type from the Axios library, and the GenerateTable function from the
GeneratedTable file. */
import React, { useState, useEffect, ChangeEvent } from "react";
import axios, { AxiosResponse } from "axios";
import { GenerateTable } from "./GeneratedTable";

/**
 * Props is an object with a text property that is a string.
 * @property {string} text - This is the text that will be displayed in the button.
 */
type Props = {
  text: string;
};

/* Exporting the FileUpload function. */
export const FileUpload = ({ text }: Props) => {
  /* Declaring the state variables that will be used in the component. */
  const [fileSelected, setFileSelected] = useState<File>();
  const [fileName, setFileName] = useState(String);
  const [responseData, setResponseData] = useState([]);
  const url = "http://0.0.0.0:5000/";

/**
 * A function that takes in an event and sets the file selected to the first file in the file list.
 * @param e - ChangeEvent<HTMLInputElement>
 * @returns The file that was selected.
 */
  const onFileInputChange = (e: ChangeEvent<HTMLInputElement>) => {
    const fileList = e.target.files;
    if (!fileList) return;
    console.log(fileList[0]);
    setFileSelected(fileList[0]);
  };

  /**
   * It takes a file, sends it to the server, and then returns the response data
   * @param {any} e - any - this is the event that is triggered when the form is submitted.
   */
  const uploadFile = async (e: any) => {
    e.preventDefault();
    if (fileSelected) {
      const formData = new FormData();
      setFileName(fileSelected.name);
      formData.append("file", fileSelected, fileSelected.name);
      await axios
        .post(`${url}upload`, formData, {
          headers: {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS",
            "Content-Type": "multipart/form-data",
            "Access-Control-Allow-Credentials": true,
          },
        })
        .then((response: AxiosResponse) => {
          // then print response status
          console.log("response OK", response);
          setResponseData(response.data.payrollReport.employeeReports);
          return response;
        })
        .catch((error) => {
          console.log("error", error);
          return Promise.reject(error);
        });
    }
  };

  /* A hook that is called after every render. It is used to perform side effects. */
  useEffect(() => {
    console.log("responseData", responseData);
  }, [responseData]);

  return (
    <div className="my-20 content-start">
      <div className="title">
        <h1 className="text-5xl font-black text-white text-center">
          <span className="text-slate-900">{text}</span>
        </h1>
      </div>
      <div className="my-20">
        <form>
          <input type="file" accept=".csv" onChange={onFileInputChange} />
          <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded"
            onClick={uploadFile}
          >
            Upload
          </button>
        </form>
      </div>

     { /* Rendering the GenerateTable component. */}
      <div className="my-20 content-start">
        {responseData && fileName && GenerateTable(fileName, responseData)}
      </div>
    </div>
  );
};
