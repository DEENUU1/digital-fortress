/** @type {import('next').NextConfig} */
const nextConfig = {
    "env": {
        "API_URL": process.env.API_URL,
        "NEXT_PUBLIC_HOST": process.env.NEXT_PUBLIC_HOST
    },
    typescript: {
        ignoreBuildErrors: true,
    },
};

export default nextConfig;
