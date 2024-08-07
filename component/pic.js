const context = require.context("@/assets/", false, /\.jpg$/);
const images = context.keys().map(context);

export default images;

