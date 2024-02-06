import "./globals.css";
import { ReactNode } from "react";
import Provider from "@/redux/provider";
import Setup from "@/components/utils/Setup";
interface IProps {
  children: ReactNode;
}
export default function RootLayout({ children }: IProps) {
  return (
    <html lang="en">
      <body>
        <Provider>
          <Setup />

          {/*<Navbar />*/}
          {children}
          {/*<Footer />*/}
        </Provider>
      </body>
    </html>
  );
}