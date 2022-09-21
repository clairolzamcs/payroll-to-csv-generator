/* A function that takes in two parameters, fileName and TableItems. It returns a table that is
generated from the data in the file. */
export const GenerateTable = (fileName: string, TableItems: any) => {
  return (
    <>
      <div className="flex flex-col">
        <div className="overflow-x-auto">
          <div className="p-1.5 w-full inline-block align-middle">
            <div className="overflow-hidden border rounded-lg">
              <h1 className="text-lg font-black text-white text-center">
                <span className="text-slate-900">
                  Generated Report from {fileName}
                </span>
              </h1>
              <table className="min-w-full divide-y divide-gray-200">
                <thead className="bg-gray-50">
                  <tr>
                    <th
                      scope="col"
                      className="px-6 py-3 text-xs font-bold text-left text-gray-500 uppercase "
                    >
                      Employee ID
                    </th>
                    <th
                      scope="col"
                      className="px-6 py-3 text-xs font-bold text-left text-gray-500 uppercase "
                    >
                      Payroll Start Date
                    </th>
                    <th
                      scope="col"
                      className="px-6 py-3 text-xs font-bold text-left text-gray-500 uppercase "
                    >
                      Payroll End Date
                    </th>
                    <th
                      scope="col"
                      className="px-6 py-3 text-xs font-bold text-right text-gray-500 uppercase "
                    >
                      Total Amount Paid
                    </th>
                  </tr>
                </thead>

                <tbody className="divide-y divide-gray-200">
                  {TableItems.map((list: any, index: any) => {
                    return (
                      <tr key={index}>
                        <td className="px-6 py-4 text-sm font-medium text-gray-800 whitespace-nowrap">
                          {list.employeeID}
                        </td>
                        <td className="px-6 py-4 text-sm text-gray-800 whitespace-nowrap">
                          {list.payPeriod.startDate}
                        </td>
                        <td className="px-6 py-4 text-sm text-gray-800 whitespace-nowrap">
                          {list.payPeriod.endDate}
                        </td>
                        <td className="px-6 py-4 text-sm font-medium text-right whitespace-nowrap">
                          <a
                            className="text-green-500 hover:text-green-700"
                            href="#"
                          >
                            ${list.amountPaid}
                          </a>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};
