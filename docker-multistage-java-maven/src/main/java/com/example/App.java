package com.example;

import com.sun.net.httpserver.HttpServer;
import java.io.IOException;
import java.net.InetSocketAddress;

public class App {

    public static void main(String[] args) throws IOException {

        HttpServer server = HttpServer.create(
                new InetSocketAddress(8080), 0
        );

        server.createContext("/", exchange -> {

            String response = """
                    {
                      "message": "Docker Multi-Stage App",
                      "status": "running"
                    }
                    """;

            exchange.getResponseHeaders()
                    .set("Content-Type", "application/json");

            exchange.sendResponseHeaders(
                    200,
                    response.getBytes().length
            );

            exchange.getResponseBody()
                    .write(response.getBytes());

            exchange.close();
        });

        server.start();

        System.out.println(
                "Server running on port 8080"
        );
    }
}