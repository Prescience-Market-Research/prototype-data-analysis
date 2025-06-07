var dagcomponentfuncs = (window.dashAgGridComponentFunctions =
  window.dashAgGridComponentFunctions || {});

const productSpecRules = {
  Provider: [
    { value: "Telstra", label: "Telstra" },
    { value: "Optus", label: "Optus" },
    { value: "Vodafone", label: "Vodafone" },
    { value: "Belong", label: "Belong" },
    {
      value: "Everyday Mobile (from Woolworths)",
      label: "Everyday Mobile (from Woolworths)",
    },
    { value: "JB Hi Fi", label: "JB Hi Fi" },
    { value: "Aldi", label: "Aldi" },
    { value: "Boost", label: "Boost" },
    { value: "Amaysim", label: "Amaysim" },
  ],

  "Plan Type": [
    { value: "Month to Month", label: "Month to Month" },
    { value: "Pre-Paid Cap", label: "Pre-Paid Cap" },
    { value: "Pre-Paid Bulk Buy", label: "Pre-Paid Bulk Buy" },
  ],

  "No Contract": {
    "Month to Month": [
      { value: "Not available", label: "Not available" },
      { value: "No contract", label: "No contract" },
    ],
    "Pre-Paid Cap": [{ value: "NA", label: "NA" }],
    "Pre-Paid Bulk Buy": [{ value: "NA", label: "NA" }],
  },
  "12 Month Contract": {
    "Month to Month": [
      { value: "Not available", label: "Not available" },
      { value: "12 Month Contract", label: "12 Month Contract" },
    ],
    "Pre-Paid Cap": [{ value: "NA", label: "NA" }],
    "Pre-Paid Bulk Buy": [{ value: "NA", label: "NA" }],
  },
  "24 Month Contract": {
    "Month to Month": [
      { value: "Not available", label: "Not available" },
      { value: "24 Month Contract", label: "24 Month Contract" },
    ],
    "Pre-Paid Cap": [{ value: "NA", label: "NA" }],
    "Pre-Paid Bulk Buy": [{ value: "NA", label: "NA" }],
  },
  "36 Month Contract": {
    "Month to Month": [
      { value: "Not available", label: "Not available" },
      { value: "36 Month Contract", label: "36 Month Contract" },
    ],
    "Pre-Paid Cap": [{ value: "NA", label: "NA" }],
    "Pre-Paid Bulk Buy": [{ value: "NA", label: "NA" }],
  },

  "Minimum Monthly Spend": {
    "Month to Month": [
      { value: "$25", label: "$25" },
      { value: "$50", label: "$50" },
      { value: "$60", label: "$60" },
      { value: "$70", label: "$70" },
      { value: "$80", label: "$80" },
      { value: "$100", label: "$100" },
      { value: "$125", label: "$125" },
    ],
    "Pre-Paid Cap": [
      { value: "$25", label: "$25" },
      { value: "$50", label: "$50" },
      { value: "$60", label: "$60" },
      { value: "$70", label: "$70" },
      { value: "$80", label: "$80" },
      { value: "$100", label: "$100" },
      { value: "$125", label: "$125" },
    ],
    "Pre-Paid Bulk Buy": [
      { value: "$50", label: "$50" },
      { value: "$100", label: "$100" },
      { value: "$365", label: "$365" },
    ],
  },
};

dagcomponentfuncs.OptionComponent = function (props) {
  const colName = props.colDef.field;
  const rowData = props.data;
  let options = productSpecRules[colName];

  // if options is an object, we need to handle it differently
  if (typeof options === "object" && !Array.isArray(options)) {
    const planType = rowData["Plan Type"];
    options = productSpecRules[colName][planType] || [];
  }

  return React.createElement(
    "select",
    {
      onChange: function (event) {
        props.setValue(event.target.value); // Update the value in Dash
      },
      value: props.value,
      style: {
        padding: "5px",
        border: "1px solid #ccc",
        borderRadius: "4px",
        backgroundColor: "#f9f9f9",
        color: "#333",
        fontSize: "14px",
        width: "100%",
      },
    },
    options.map(function (option) {
      return React.createElement(
        "option",
        { key: option.value, value: option.value },
        option.label
      );
    })
  );
};
