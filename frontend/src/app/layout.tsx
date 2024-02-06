import "./globals.css";
import { ReactNode } from "react";
import Provider from "@/redux/provider";
import Setup from "@/components/utils/Setup";
import Header from "@/components/layout/Header"
import Footer from "@/components/layout/Footer"

interface IProps {
  children: ReactNode;
}
export default function RootLayout({ children }: IProps) {
  return (
    <html lang="en">
      <body>
        <Provider>
          <Setup />

          <Header />
          {children}
          <Footer/>
        </Provider>
      </body>
    </html>
  );
}