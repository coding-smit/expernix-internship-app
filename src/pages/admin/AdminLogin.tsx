import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import { ArrowLeft, Shield } from "lucide-react";

import { useToast } from "@/hooks/use-toast";

const AdminLogin = () => {

  const navigate = useNavigate();

  const { toast } = useToast();

  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  const handleSubmit = async (e: React.FormEvent) => {

    e.preventDefault();

    try {

      const response = await fetch(
        "https://api.expernix.in/api/admin-login/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(formData),
        }
      );

      const data = await response.json();

      if (response.ok) {

        localStorage.setItem("token", data.token);

        toast({
          title: "Login Successful",
          description: "Welcome Admin!",
        });

        navigate("/admin/dashboard");

      } else {

        toast({
          title: "Login Failed",
          description: data.error,
          variant: "destructive",
        });

      }

    } catch (error) {

      toast({
        title: "Server Error",
        description: "Backend not responding",
        variant: "destructive",
      });

    }
  };

  return (
    <div className="min-h-screen gradient-hero flex items-center justify-center p-4">

      <div className="w-full max-w-md">

        <Link
          to="/"
          className="inline-flex items-center gap-2 text-muted-foreground hover:text-foreground mb-8 transition-colors"
        >
          <ArrowLeft className="w-4 h-4" />
          Back to Home
        </Link>

        <Card>

          <CardHeader className="text-center pb-2">

            <div className="w-12 h-12 rounded-xl gradient-primary flex items-center justify-center mx-auto mb-4">
              <Shield className="w-6 h-6 text-primary-foreground" />
            </div>

            <CardTitle className="text-2xl">
              Admin Login
            </CardTitle>

            <CardDescription>
              Sign in to access admin dashboard
            </CardDescription>

          </CardHeader>

          <CardContent>

            <form onSubmit={handleSubmit} className="space-y-4">

              <div className="space-y-2">

                <Label htmlFor="email">
                  Username
                </Label>

                <Input
                  id="email"
                  type="text"
                  placeholder="Enter username"
                  value={formData.email}
                  onChange={(e) =>
                    setFormData({
                      ...formData,
                      email: e.target.value,
                    })
                  }
                  required
                />

              </div>

              <div className="space-y-2">

                <Label htmlFor="password">
                  Password
                </Label>

                <Input
                  id="password"
                  type="password"
                  placeholder="••••••••"
                  value={formData.password}
                  onChange={(e) =>
                    setFormData({
                      ...formData,
                      password: e.target.value,
                    })
                  }
                  required
                />

              </div>

              <Button
                type="submit"
                className="w-full"
              >
                Sign In
              </Button>

            </form>
            <div className="mt-6 text-center"> 
              <p className="text-sm text-muted-foreground"> 
                Are you an intern?{" "} 
                <Link to="/intern/login" className="text-primary hover:underline"> Login here </Link>
                 </p> </div>
          </CardContent>

        </Card>

      </div>

    </div>
  );
};

export default AdminLogin;