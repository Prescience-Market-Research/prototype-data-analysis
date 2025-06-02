var dagcomponentfuncs = (window.dashAgGridComponentFunctions =
  window.dashAgGridComponentFunctions || {});

dagcomponentfuncs.StockLink = function (props) {
  console.log("dagcomponentfuncs.StockLink", props);

  return React.createElement(
    "a",
    { href: "https://finance.yahoo.com/quote/" + "sds" },
    props.value
  );
};
dagcomponentfuncs.OptionComponent = function (props) {
  console.log("dagcomponentfuncs.OptionComponent", props);

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
    props.options.map(function (option) {
      return React.createElement(
        "option",
        { key: option.value, value: option.value },
        option.label
      );
    })
  );
};
