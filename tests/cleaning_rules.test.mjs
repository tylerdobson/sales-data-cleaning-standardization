import assert from "node:assert/strict";

function cleanText(value) {
  return String(value ?? "").replace(/\s+/g, " ").trim();
}

function isCancellation(invoice) {
  return cleanText(invoice).toUpperCase().startsWith("C");
}

function parseDate(value) {
  const text = cleanText(value);
  const match = text.match(/^(\d{1,2})\/(\d{1,2})\/(\d{4})\s+(\d{1,2}):(\d{2})$/);
  if (match) {
    const [, day, month, year, hour, minute] = match;
    const d = new Date(Date.UTC(Number(year), Number(month) - 1, Number(day), Number(hour), Number(minute), 0));
    return Number.isNaN(d.getTime()) ? null : d;
  }
  return null;
}

function canonicalKey(row) {
  return [
    cleanText(row.invoice),
    cleanText(row.stock_code).toUpperCase(),
    cleanText(row.description),
    row.quantity,
    row.invoice_date,
    row.unit_price,
    cleanText(row.customer_id),
    cleanText(row.country),
  ].join("|");
}

assert.equal(cleanText("  EIRE  "), "EIRE");
assert.equal(cleanText("white   cherry   lights"), "white cherry lights");
assert.equal(isCancellation("C489449"), true);
assert.equal(isCancellation("489434"), false);

const parsed = parseDate("01/12/2009 07:45");
assert.ok(parsed);
assert.equal(parsed.toISOString(), "2009-12-01T07:45:00.000Z");

const left = canonicalKey({
  invoice: " 489434 ",
  stock_code: "85048",
  description: "15CM CHRISTMAS GLASS BALL 20 LIGHTS",
  quantity: 12,
  invoice_date: "2009-12-01T07:45:00.000Z",
  unit_price: 6.95,
  customer_id: "13085",
  country: " United Kingdom ",
});
const right = canonicalKey({
  invoice: "489434",
  stock_code: "85048",
  description: "15CM CHRISTMAS GLASS BALL 20 LIGHTS",
  quantity: 12,
  invoice_date: "2009-12-01T07:45:00.000Z",
  unit_price: 6.95,
  customer_id: "13085",
  country: "United Kingdom",
});
assert.equal(left, right);

console.log("Cleaning rule checks passed.");
