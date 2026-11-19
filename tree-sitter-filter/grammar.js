module.exports = grammar({
  name: 'filter',
  extras: $ => [/\s/],

  rules: {
    query: $ => $.comparison,

    comparison: $ => seq(
      $.identifier,
      choice('=', '!=', '>', '<', '>=', '<='),
      $._value,
    ),

    _value: $ => choice($.string, $.number),
    string: $ => /"[^"]*"/,
    number: $ => /\d+(\.\d+)?/,
    identifier: $ => /[a-zA-Z_][a-zA-Z0-9_.]*/,
  }
});
