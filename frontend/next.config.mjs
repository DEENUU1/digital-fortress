/** @type {import('next').NextConfig} */
const nextConfig = {
    "env": {
        "API_URL": process.env.API_URL,
    },
    typescript: {
        ignoreBuildErrors: true,
    },
};

export default nextConfig;
